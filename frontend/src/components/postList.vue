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
          <Input :return="inputEmail" label='Email' Type='text'/>
          <Input :return="inputPassword" label='Password' Type='password'/>
        </div>
        <span class="error" style="align-self: flex-start">{{ error }}</span>
      </div>
      <div class="button-group">
        <button class="btn secondary">Cadastrar</button>
        <button class="btn primary" @click="teste()">Login</button>
      </div>
    </div>
  </section>
</template>

<script>
import { getAll } from '../api/post'
export default {
  data () {
    return {
      email: '',
      password: '',
      error: null
    }
  },
  methods: {
    async teste () {
      try {
        this.error = null
        const res = await getAll()
        if (!res.Sucess) this.error = res.Cause
        console.log(res)
      } catch (error) {
        console.log(new Error(error))
      }
    }
  }
}
</script>
