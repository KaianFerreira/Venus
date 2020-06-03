<template>
  <section class="container">
    <div class="login-form">
      <div class="wrapper">
        <div class="header">
          <div class="logo">
            Venus
          </div>
          <div class="title">Login</div>
        </div>
        <div class="input-group">
          <Input :return="inputUser" label='Consultar posts usuario' Type='text'/>
        </div>
        <span class="error" style="align-self: flex-start">{{ error }}</span>
      </div>
      <div class="button-group">
        <button class="btn secondary" @click="postListUser()" >Listar usuario</button>
        <button class="btn primary" @click="postList()">Login</button>
      </div>
      <div v-for="post in posts" :key="post.id">
        {{ post.description }}: {{ post.link }}
      </div>
    </div>
  </section>
</template>

<script>
import { getAll, getAllUser } from '../api/post'
export default {
  data () {
    return {
      user: '',
      posts: [],
      error: null
    }
  },
  methods: {
    inputUser (value) {
      this.user = value
    },
    async postList () {
      try {
        this.error = null
        const res = await getAll()
        if (!res.Sucess) this.error = res.Cause
        this.posts = res.posts
        // console.log(this.posts)
      } catch (error) {
        console.log(new Error(error))
        console.log('Deu erro')
      }
    },
    async postListUser () {
      try {
        this.error = null
        const res = await getAllUser(this.user)
        if (!res.Sucess) this.error = res.Cause
      } catch (error) {
        console.log(new Error(error))
      }
    }
  }
}
</script>
