<template>
  <section class="container">
    <div class="content" v-if="loaded">
      <div class="list flex" v-for="post in posts" :key="post.id">
        <div class="post flex">
          <div class="rating">
            <div class="vote flex">
              <div class="icon-wrapper" @click="upvote(post.id)">
                <IconUpVote css="icon up black"/>
              </div>
            </div>
            {{ post.upvotes }}
            <div class="vote flex">
              <div class="icon-wrapper" @click="upvote(post.id)">
                <IconUpVote css="icon down rotate black"/>
              </div>
            </div>
          </div>
          <div class="post-wrapper">
            <span>Postado por {{ post.username }}</span>
            <div class="post-header">
              <span>{{ post.title }}</span>
            </div>
            <div class="post-content">
              <span>{{ post.description }}</span>
            </div>
            <div class="post-footer">
              <a class="link" :href="post.link"> {{post.link}} </a>
              <button v-if="post.username === user.name" @click="remove(post.id)"> Deletar </button>
              <button v-if="post.username === user.name"> Editar </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { getAll, getAllUser, upvote, remove } from '../../api/post'
import { mapState } from 'vuex'
export default {
  data () {
    return {
      posts: [],
      error: null
    }
  },
  computed: {
    ...mapState(['user', 'loaded'])
  },
  mounted () {
    console.log(this.user)
    this.postList()
  },
  methods: {
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
    },
    open (link) {
      window.open(link, '_blank')
    }
  }
}
</script>
<style lang="scss" scoped>
@import '../../assets/_scss/variables.scss';
  .flex {
    display: flex;
  }
  .content {
    width: 100%;
    // min-height: 100%;
    padding: 20px 0px;
    .list {
      justify-content: center;
    }
    .post {
      border: 1px solid #c4c4c4;
      border-radius: 20px;
      width: 100%;
      margin: 20px;
      padding: 20px;
      .rating {
        font-size: 0.8em;
        text-align: center;
        margin-right: 10px;
        .vote {
          align-items: center;
          justify-content: center;
        }
        .icon {
          svg path {
            transition: 0.33s !important;
          }
          width: 15px;
          &.up {
            transform: rotate(-90deg);
            &:hover {
              fill: $primary-color;
              }
          }
          &.down {
            transform: rotate(90deg);
            &:hover {
              fill: red;
            }
          }
        }
      }
      .post-header {
        font-weight: bold;
      }
      .post-content {
        margin: 10px 0px;
      }
      .link {
        transition: 0.33s;
        cursor: pointer;
        &:hover {
          color: $primary-color;
        }
      }
    }
  }
</style>
