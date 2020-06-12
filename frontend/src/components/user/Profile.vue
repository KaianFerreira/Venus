<template>
  <section class="container">
    <div class="content">
      <h1> Perfil de {{ this.userProfile.name }} </h1>
      <br>
      <h4> Total de seguidores {{ this.userFollowers }} | Total de upvotes {{ this.userUpvotes }}</h4>
      <br>
      <div v-if="followable !== null" class="button-group" >
          <button class="btn primary" @click="follow(userProfile.name)">{{ this.followable }}</button>
      </div>
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
        </div>
        <a> {{ post.username }} </a>
      </div>
    </div>
  </section>
</template>

<script>
import { getAllUser, follow, upvote } from '../../api/post'
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState(['user'])
  },
  data () {
    return {
      userProfile: '',
      posts: [],
      userFollowers: 0,
      userUpvotes: 0,
      followable: null,
      error: null
    }
  },
  props: ['username'],
  components: {
  },
  mounted () {
    this.postList()
  },
  methods: {
    async postList () {
      try {
        this.error = null
        const res = await getAllUser(this.username)
        if (!res.Sucess) this.error = res.Cause
        this.posts = res.posts
        this.userProfile = res.user
        if (this.userProfile.name === this.user.name) {
          this.followable = null
        } else {
          this.followable = res.followable
        }
        console.log(this.followable)
        this.userFollowers = res.user_followers
        this.userUpvotes = res.user_upvotes

        // console.log(this.posts)
      } catch (error) {
        console.log(new Error(error))
        console.log('Deu erro')
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
    async follow (id) {
      try {
        this.error = null
        const res = await follow(id)
        if (!res.Sucess) this.error = res.Cause
      } catch (error) {
        console.log(new Error(error))
      }
      this.postList()
    }
  }
}
</script>

<style lang="scss" scoped>
  @import '../../assets/_scss/variables.scss';
  .container {
    border: 3px
  }
  h1{
      margin-left: 40%;
  }
  h4{
      margin-left: 37%;
  }
  .content {
    width: 100%;
    //min-height: 100%;
    padding: 20px;
  }
  .btn{
      margin-left: 44.5%;
  }
</style>
