<template>
  <section class="container">
    <div class="login-form">
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
      <div class="button-group">
        <button class="btn secondary">Cadastrar</button>
        <button class="btn primary">Login</button>
      </div>
    </div>
  </section>
</template>

<script>
import Input from './Input'
export default {
  components: {
    Input
  },
  data () {
    return {
      login: true,
      email: null,
      password: null,
      name: null,
      lastName: null
    }
  },
  methods: {
    inputEmail (value) {
      this.email = value
    },
    inputPassword (value) {
      this.password = value
    },
    signIn () {
      console.log('logar')
    },
    signUp () {
      console.log('cadastro')
    }
  }
}
</script>

<style lang="scss" scoped>
@import "../assets/_scss/variables.scss";
  .login-form {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
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
        width: 100px;
        height: 50px;
        font-size: 1.6em;
        justify-content: center;
        border-left: 6px solid #0049FF;
      }
    }
    .input-group {
      margin-bottom: 70px;
    }
  }
  @media screen and (min-width: $desktop-width) {
    .input-group {
      font-size: 15px;
    }
  }
</style>
