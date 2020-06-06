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
          <button class="btn primary" @click="upvote()">Up</button>
        </div>
        {{ post }}
      </div>
  </section>
</template>

<script>
import { getAll, getAllUser } from '../../api/post'
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
    }
  }
}
</script>
