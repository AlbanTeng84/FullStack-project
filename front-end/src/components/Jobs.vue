<!-- <template>
  <div>
    <p>{{ dataRetrive }}</p>
    <p>{{ username }}</p>
    <p>{{ password }}</p>
    <form @submit="userSubmit" method="post">
      <div class="input_user">
        <label>UserName: </label>
        <input type="text" v-model="posts.username">
      </div>
      
      <div class="input_pwd">
        <label>Password: </label>
        <input  type="password" v-model="posts.password">  
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return{
        dataRetrive: '',
       
    }
  },

  methods:{
    // userSubmit(e){
    //   this.axios.posts('http://127.0.0.1:5000/posts', this.posts)
    //     .then(result =>{
    //       console.log(result.data)
    //     })
    //   e.preventDefault()

    // },
    userGet(){
      axios.get('http://127.0.0.1:5000/jobs')
      .then(res => {
        console.log(res)
      
      })
    }
   
  },
  mounted(){
    this.userGet()

  }
    
}
</script>

<style>
  form {
    font-weight: bold;
    color: blue;
    text-decoration: none;
    padding:50px;
    border-radius: 4px;
  }
  .input_user {
    font-weight: bold;
    color: white;
    text-decoration: none;
    padding:30px;
    border-radius: 4px;
  }
  .input_pwd {
    font-weight: bold;
    color: white;
    text-decoration: none;
    padding:10px;
    border-radius: 4px;
  }
</style> -->