<template>
  <section class="container">
    <div class="content">
      <div>
        <div class="wrapper">
          <div class="header">
          </div>
          <div class="input-group-post">
            <Input v-model="title" label='Titulo da publicação' Type='text'/>
            <Input v-model="descricao" label='Descricao' Type='text'/>
            <Input v-model="link" label='Link de referencia' Type='text'/>
          </div>
          <span class="error" style="align-self: flex-start">{{ error }}</span>
        </div>
        <div class="button-group">
          <button class="btn primary" @click="insertPost()">Postar</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { create } from '../../api/post'

export default {
  data () {
    return {
      descricao: '',
      link: '',
      title: '',
      error: null
    }
  },
  props: ['reload'],
  methods: {
    async insertPost () {
      try {
        this.error = null
        const res = await create(this.descricao, this.link, this.title)
        this.descricao = null
        this.link = null
        this.title = null
        if (!res.Sucess) this.error = res.Cause
        this.reload()
        console.log(res)
      } catch (error) {
        console.log(new Error(error))
      }
    }
  }
}
</script>

<style lang="scss" scoped>
  @import '../../assets/_scss/variables.scss';
  .container {
    border-style: solid;
    border-width: 5px;
    border-color: black;
    width: 50%;
    margin-left: 30%
  }
  .content {
    width: 100%;
    min-height: 100%;
    padding: 20px;
  }
</style>
