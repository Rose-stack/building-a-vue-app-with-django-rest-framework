<template>
<div class="todos_container">
    <div class="add_todo">
        <form v-on:submit.prevent="submitForm">
            <div class="form-group">
                <label for="title">Title</label>
                <input type="text" class="form-control" id="title" v-model="title">
            </div>
            <div class="form-group">
                <label for="description">Description</label>
                <textarea class="form-control" id="description" v-model="description"></textarea>
            </div>
            <div class="form-group">
                <button type="submit">Add Todo</button>
            </div>
        </form>
    </div>
    <div class="todos_content">
    <h1>Todos</h1>
    <ul class="todos_list">
        <li v-for="todo in todos" :key="todo.id">
        <h2>{{ todo.title }}</h2>
        <p>{{ todo.description }}</p>
        <button @click="toggleTodo(todo)">
            {{ todo.completed ? 'Undo' : 'Complete' }}
        </button>        
        <button @click="deleteTodo(todo)">Delete</button>
        </li>
    </ul>
    </div>
</div>
</template>
<script>
export default {
 data(){
   return {
     todos:[],
     title:'',
     description:''
   }
 },
  methods: {
    async getData(){
      try{
        const response = await this.$http.get('http://localhost:8000/api/todos/');
        this.todos = response.data;
      }catch(error){
        console.log(error);
      }
    },
    async submitForm(){
      try{
        const response = await this.$http.post('http://localhost:8000/api/todos/', {
          title: this.title,
          description: this.description,
          completed:false
        });
        this.todos.push(response.data);
        this.title = '';
        this.description = '';
      }catch(error){
        console.log(error);
      }
    },
    async toggleTodo(todo){
        try{
            const response = await this.$http.put(`http://localhost:8000/api/todos/${todo.id}/`, {
                completed: !todo.completed,
                title: todo.title,
                description: todo.description
            });
            let todoIndex = this.todos.findIndex(t => t.id === todo.id);
            this.todos = this.todos.map((todo) => {
                if(this.todos.findIndex(t => t.id === todo.id) === todoIndex){
                    return response.data;
                }
                return todo;
            });
        }catch(error){
            console.log(error);
        }
    },
    async deleteTodo(todo){
      let confirmation = confirm("Do you want to delete this todo?");

      if(confirmation){
        try{
        await this.$http.delete(`http://localhost:8000/api/todos/${todo.id}`);
        // refresh the todos
        this.getData();
      }catch(error){
        console.log(error)
      }
      }      
    }
  },

  created(){
    this.getData();
  }
}
</script>