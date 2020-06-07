<template>
  <section class="container">
      <div class="wrapper">
        <span class="error" style="align-self: flex-start">{{ error }}</span>
      </div>
      <div v-for="follower in followers" :key="follower">
        <p>{{ follower.followed }}</p>
      </div>
       <div v-for="followed in following" :key="followed.id">
        <p>{{ followed.followed }}</p>
      </div>
  </section>
</template>

<script>
import { social } from '../../api/post'
export default {
  data () {
    return {
      user: '',
      followers: [],
      following: [],
      error: null
    }
  },
  mounted () {
    this.social()
  },
  methods: {
    inputUser (value) {
      this.user = value
    },
    async social () {
      try {
        this.error = null
        const res = await social()
        if (!res.Sucess) this.error = res.Cause
        this.followers = res.followers
        this.following = res.following
        console.log(this.following)
      } catch (error) {
        console.log(new Error(error))
        console.log('Deu erro')
      }
    }
  }
}
</script>
