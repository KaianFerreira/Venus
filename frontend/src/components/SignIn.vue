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
                <input type="email" class="input-value input-large" id="email" v-model="email"/>
                <label class="input-span" for="email" :class="{ 'active': email }">Email</label>
                <div class="line"></div>
              </div>
              <div class="form-group">
                <input type="password" class="input-value input-large"  id="password" v-model="password">
                <label class="input-span" :class="{ 'active': password }" for="password">Senha</label>
                <div class="line"></div>
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
  background-color: #666666;
  color: white;
  display: flex;
  height: 100%;
  width: 500px;
  justify-content: center;
  padding: 30px;
  .wrapper {
    min-height: 100%;
  }
  .header {
    display: flex;
    justify-content: center;
    width: 100%;
    * {
      border: 1px solid white;
    }
  }
}
</style>
