<template>
  <section class="container login">
    <form @submit.prevent="signIn" class="login-form">
      <div class="wrapper">
        <div class="header">
          <Logo/>
          <div class="title">Login</div>
        </div>
        <div class="input-group">
          <Input v-model="email" label='Email' Type='text'/>
          <Input v-model="password" label='Password' Type='password'/>
        </div>
        <span class="error" style="align-self: flex-start">{{ error }}</span>
      </div>
      <div class="button-group">
        <button type="button" @click="$router.push('/signup')" name="register" class="btn secondary">Cadastrar</button>
        <button type="submit" name="login" class="btn primary">Login</button>
      </div>
    </form>
  </section>
</template>

<script>

import { login } from '../api/core'
export default {
  data () {
    return {
      email: '',
      password: '',
      error: null
    }
  },
  methods: {
    async signIn () {
      try {
        this.error = null
        const res = await login(this.email, this.password)
        this.$store.dispatch('signIn', res)
      } catch (error) {
        this.error = error.response ? error.response.data.cause : {}
        console.log(new Error(error))
      }
    }
  }
}
</script>
