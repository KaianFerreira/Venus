<template>
  <div class="form-group">
    <div v-if="Type === 'text'" class="wrapper">
      <input type="text" class="input-value" id="text" v-model="value"/>
      <label class="input-span" for="email" :class="{ 'active': value }">{{ label }}</label>
      <div class="line"></div>
    </div>
    <div v-if="Type === 'email'" class="wrapper">
      <input type="email" class="input-value" id="email" v-model="value"/>
      <label class="input-span" for="email" :class="{ 'active': value }">{{ label }}</label>
      <div class="line"></div>
    </div>
    <div v-if="Type === 'password'" class="wrapper">
      <input type="password" class="input-value" id="password" v-model="value"/>
      <label class="input-span" for="password" :class="{ 'active': value }">{{ label }}</label>
      <div class="line"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['return', 'label', 'Type'],
  watch: {
    value () {
      this.return(this.value)
    }
  },
  data () {
    return {
      type: 'text',
      value: null
    }
  }
}
</script>

<style>
  .wrapper {
    display: flex;
    flex-direction: column;

  }
</style>
