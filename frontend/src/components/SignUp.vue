<template>
  <section class="container">
    <div class="login-form">
      <div class="wrapper">
        <div class="header">
          <div class="logo">
            Venus
          </div>
          <div class="title">Cadastro</div>
        </div>
        <div class="input-group">
          <Input :return="inputEmail" label='Email' Type='text'/>
          <Input :return="inputPassword" label='Senha' Type='password'/>
          <Input :return="inputPasswordConfirmation" label='Confirme a senha' Type='password'/>
        </div>
        <span class="error" style="align-self: flex-start">{{ error }}</span>
      </div>
      <div class="button-group">
        <button @click="$router.push('/signin')" class="btn secondary">Cancelar</button>
        <button @click="signUp()" class="btn primary">Continuar</button>
      </div>
    </div>
  </section>
</template>

<script>
import Input from './Input'
import { singup } from '../api/core'
export default {
  components: {
    Input
  },
  data () {
    return {
      login: true,
      email: '',
      password: '',
      error: null,
      passwordConfirmation: null
    }
  },
  methods: {
    inputEmail (value) {
      this.email = value
    },
    inputPassword (value) {
      this.password = value
    },
    inputPasswordConfirmation (value) {
      this.passwordConfirmation = value
    },
    async signUp () {
      try {
        if (this.password !== this.passwordConfirmation) this.error = 'Confirmação de senha inválida'
        else {
          this.error = null
          const res = await singup(this.login, this.password)
          if (!res.sucess) this.error = res.cause
          else throw new Error(res.cause)
        }
      } catch (error) {
        this.error = error
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
    .wrapper {
      width: 100%;
      height: 500px;
      display:flex;
      flex-direction: column;
      align-items: center;
    }
    .header {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
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
        justify-content: center;
        padding-left: 10px;
        border-left: 6px solid #0049FF;
      }
    }
    .input-group {
      width: 100%;
    }
  }
  @media screen and (min-width: $desktop-width) {
    .container {
      display: flex;
      justify-content: flex-end;
      align-items: flex-start;
      height: 100%;
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
