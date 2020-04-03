<template>
  <section class="container">
    <div class="login-form">
      <div class="wrapper">
        <div class="header">
          <div @click="login = true">Entrar</div>
          <div @click="login = false">Registrar-se</div>
        </div>
        <div class="content">
          <div v-if="login" class="login-form">
            <form @submit.prevent="signIn">
              <div class="form-group">
                <input type="email" class="input-large" placeholder="Email" v-model="email">
              </div>
              <div class="form-group">
                <input type="password" class="input-large" placeholder="Senha" v-model="password">
              </div>
            </form>
          </div>
          <div v-if="!login" class="signUp">
            <form @submit.prevent="signUp">

            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
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
.container {
  display: flex;
  justify-content: center;
  height: 100%;
  min-width: 100%;
  align-items: center;
}
.login-form {
  background-color: #0e002f;
  color: white;
  display: flex;
  justify-content: center;
  .wrapper {
    width: 300px;
  }
  .header {
    display: flex;
  }
  .content {
  }
}
</style>
