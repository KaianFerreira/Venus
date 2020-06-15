<template>
  <section class="container">
    <div class="content" v-if="loaded">
      <!-- <InsertPost :reload="this.postList" /> -->
      <InsertPost :popup="popup" v-if="popup.open"/>
      <div class="search-wrapper">
        <div class="input-search">
          <input type="text" v-model="search">
          <div class="icon-wrapper">
            <IconSearch class="icon"/>
          </div>
        </div>
        <div class="icon-wrapper icon-search" @click="popup.open = true">
          <IconPlus class="icon"/>
        </div>
      </div>
      <div class="list flex" v-for="post in filteredItems" :key="post.id">
        <div class="post flex">
          <div class="rating">
            <div class="vote flex">
              <div class="icon-wrapper" @click="upvote(post.id)">
                <IconLove css="icon black"/>
              </div>
            </div>
            {{ post.upvotes }}
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
import InsertPost from '../PopUp'
// import InsertPost from './InsertPost'
export default {
  data () {
    return {
      posts: [],
      search: '',
      popup: {
        open: false,
        type: 'overdue'
      },
      error: null
    }
  },
  computed: {
    ...mapState(['user', 'loaded']),
    filteredItems () {
      return this.posts.filter(x => Object.keys(x).some(key => String(x[key]).toUpperCase().includes(this.search.toUpperCase())))
    }
  },
  components: {
    // InsertPost,
    InsertPost
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
  .search-wrapper {
    padding:0px 20px;
    display: flex;
    .icon-search {
      position: fixed;
      bottom: 20px;
      right: 20px;
      .icon {
        width: 70px;
        height: 70px;
      }
    }
    :last-child {
      .icon {
        // margin-left: 20px;
        fill: $primary-color;
      }
    }
  }
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    // min-height: 100%;
    padding: 20px 0px;
    .list {
      width: 100%;
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
          svg, path, line {
            transition: 0s !important;
          }
          fill: $primary-color;
          &:hover {
            fill: red;
          }
          width: 15px;
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
