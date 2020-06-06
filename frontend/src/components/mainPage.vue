<template>
    <div>
        <insertPost/>
        <postList/>
    </div >
</template>

<script>
import insertPost from './user/insertPost'
import postList from './user/Posts'
export default {
  components: {
    insertPost,
    postList
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>
