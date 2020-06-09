<template>
  <section class="container login">
    <div class="login-form">
      <div class="wrapper">
        <div class="header">
          <Logo/>
          <div class="title">Cadastro</div>
        </div>
        <div class="input-group">
          <Input v-model="email" label='Email' Type='text'/>
          <Input v-model="name" label='Nome' Type='text'/>
          <Input v-model="password" label='Senha' Type='password'/>
          <Input v-model="passwordConfirmation" label='Confirme a senha' Type='password'/>
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
import { singup } from '../api/core'
export default {
  data () {
    return {
      email: '',
      name: '',
      password: '',
      error: null,
      passwordConfirmation: null
    }
  },
  methods: {
    async signUp () {
      try {
        if (this.password !== this.passwordConfirmation) this.error = 'Confirmação de senha inválida'
        else {
          this.error = null
          const res = await singup(
            this.email,
            this.name,
            this.password
          )
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
