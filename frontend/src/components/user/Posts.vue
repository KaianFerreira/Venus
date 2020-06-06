<template>
  <section class="container">
      <div class="wrapper">
        <span class="error" style="align-self: flex-start">{{ error }}</span>
      </div>
      <div v-for="post in posts" :key="post.id">
        <h1>{{ post.title }}</h1>
        <span>{{ post.link }}</span>
        <p>{{ post.description }}</p>
        <div>
          upvotes: {{ post.upvotes }}
          <button class="btn primary" @click="upvote(post.id)">{{ post.upvote }}</button>
         <button v-if="post.username == 'fernandods'" @click="remove(post.id)"> Deletar </button>
         <button v-if="post.username == 'fernandods'"> Editar  </button>
        </div>
        <a> {{ post.username }} </a>
      </div>
  </section>
</template>

<script>
import { getAll, getAllUser, upvote, remove } from '../../api/post'
export default {
  data () {
    return {
      user: '',
      posts: [],
      error: null
    }
  },
  mounted () {
    this.postList()
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
    },
    async upvote (id) {
      try {
        this.error = null
        const res = await upvote(id)
        if (!res.Sucess) this.error = res.Cause
      } catch (error) {
        console.log(new Error(error))
      }
      this.postList()
    },
    async remove (id) {
      try {
        this.error = null
        const res = await remove(id)
        if (!res.Sucess) this.error = res.Cause
      } catch (error) {
        console.log(new Error(error))
      }
      this.postList()
    }
  }
}
</script>
