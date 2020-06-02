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
        <div class="button-group">
          <button @click="$router.push('/signin')" class="btn secondary">Cancelar</button>
          <button @click="signUp()" class="btn primary">Continuar</button>
        </div>
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
    signUp () {
      console.log('tentando cadastrar')
    },
    cancel () {
      console.log('cancelando')
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
      display:flex;
      flex-direction: column;
      align-items: center;
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
        width: 100px;
        height: 50px;
        font-size: 1.6em;
        justify-content: center;
        border-left: 6px solid #0049FF;
      }
    }
    .input-group {
      margin-bottom: 70px;
      width: 100%;
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
