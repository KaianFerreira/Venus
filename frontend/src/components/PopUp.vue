<template>
  <section class="pop-up-background">
    <div class="pop-up overdue">
      <div class="container-title">
        <h1>Inserir publicação</h1>
        <div class="icon-wrapper" @click="clickCancel">
          <IconClose type="button" css='icon black'/>
        </div>
      </div>
      <!-- Message -->
    <div class="content">
      <div>
        <div class="wrapper">
          <div class="header">
          </div>
          <div class="input-group-post">
            <Input v-model="title" label='Titulo da publicação' Type='text'/>
            <Input v-model="descricao" label='Descricao' Type='text'/>
            <Input v-model="link" label='Link de referencia' Type='text'/>
          </div>
          <span class="error" style="align-self: flex-start">{{ error }}</span>
        </div>
        <div class="button-group">
          <button class="btn primary" @click="insertPost()">Postar</button>
        </div>
      </div>
    </div>
    </div>
  </section>
</template>

<script>
import { create } from '../api/post'

export default {
  props: ['popup'],
  name: 'PopUp',
  computed: {
  },
  data () {
    return {
      descricao: '',
      link: '',
      title: '',
      loading: false,
      error: null
    }
  },
  methods: {
    async insertPost () {
      try {
        this.error = null
        const res = await create(this.descricao, this.link, this.title)
        this.descricao = null
        this.link = null
        this.title = null
        if (!res.Sucess) this.error = res.Cause
        this.reload()
        console.log(res)
      } catch (error) {
        console.log(new Error(error))
      }
    },
    clickCancel (e) {
      console.log(e)
      e.stopPropagation()
      this.popup.open = false
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/_scss/variables.scss';

.container-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 50px;
}

.pop-up-background {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.42);
}

.pop-up {
  max-width: 700px;
  min-width: 700px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 1px 5px 0 rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.12);
  padding: 20px;

  .btn-close {
    color: #999;
    font-size: 1.4em;
    border: none;
    background: transparent;
    width: 20px;
    height: 20px;
    padding: 3px;
    cursor: pointer;
  }

  .message {
    padding: 20px 0 10px;
  }

  .details {
    font-size: 0.85em;
  }

  .btn {
    background-color: $secondary-color;
    border: none;
    color: #fff;
    font-weight: bold;
    padding: 10px 30px;
    margin-top: 20px;
  }

  .btn-cancel {
    background-color: #fff;
  }

  .btn-2 {
    color: $primary-color;
    background: transparent;
    border: 2px solid $primary-color;
    &:active {
      color: $secondary-color;
      border: 2px solid $secondary-color;
    }
  }
}
</style>
