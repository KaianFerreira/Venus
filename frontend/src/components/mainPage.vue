<template>
    <div>
        <insertPost/>
        <postList/>
    </div >
</template>

<script>
import insertPost from './insertPost'
import postList from './postList'
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
