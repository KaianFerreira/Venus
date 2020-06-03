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
        <button @click="$router.push('/signup')" class="btn secondary">Cadastrar</button>
        <button class="btn primary" @click="signIn()">Login</button>
      </div>
    </div>
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
    inputEmail (value) {
      this.email = value
    },
    inputPassword (value) {
      this.password = value
    },
    async signIn () {
      try {
        this.error = null
        const res = await login(this.email, this.password)
        if (!res.Sucess) this.error = res.Cause
        this.$store.dispatch('signIn', res)
        this.$router.push('/teste')
      } catch (error) {
        console.log(new Error(error))
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import "../assets/_scss/variables.scss";
  .login-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    .wrapper {
      width: 100%;
      display:flex;
      flex-direction: column;
      align-items: center;
      height: 462px;
    }
    .header {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 30px;
      .logo {
        margin: 20px 0;
        color: #00CEF5;
        font-family: Satisfy;
        font-size: 4em;
      }
      .title {
        display: flex;
        align-items: center;
        align-self: flex-start;
        height: 50px;
        font-size: 1.6em;
        padding-left: 10px;
        justify-content: center;
        border-left: 6px solid #0049FF;
      }
    }
    .input-group {
      width: 100%;
    }
    .button-group {
      margin-top: 10px;
    }
  }
  @media screen and (min-width: $desktop-width) {
    .container {
      display: flex;
      justify-content: flex-end;
      align-items: flex-start;
      height:100%;
      background-color: #0C84E8;
    }
    .input-group {
      font-size: 15px;
    }
    .login-form {
      background-color: white;
      display: flex;
      .wrapper {
        padding-top: 150px;
      }
      justify-content: flex-start;
      height: 100%;
      width: 500px;
    }
  }
</style>
