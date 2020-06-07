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
          <Input v-model="descricao" label='Descricao' Type='text'/>
          <Input v-model="link" label='Link' Type='text'/>
          <Input v-model="title" label='Title' Type='text'/>
        </div>
        <span class="error" style="align-self: flex-start">{{ error }}</span>
      </div>
      <div class="button-group">
        <button class="btn secondary">Cadastrar</button>
        <button class="btn primary" @click="insertPost()">Login</button>
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
  methods: {
    async insertPost () {
      try {
        this.error = null
        const res = await create(this.descricao, this.link, this.title)
        if (!res.Sucess) this.error = res.Cause
        console.log(res)
      } catch (error) {
        console.log(new Error(error))
      }
    }
  }
}
</script>
