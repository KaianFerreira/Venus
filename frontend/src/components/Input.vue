<template>
  <div class="form-group">
    <div v-if="Type === 'text'" class="input-wrapper">
      <input v-on:input="updateValue($event.target.value)" :value="value" type="text" class="input-value"/>
      <label class="input-span" for="text" :class="{ 'active': value }">{{ label }}</label>
      <div class="line"></div>
    </div>
    <div v-if="Type === 'email'" class="input-wrapper">
      <input v-on:input="updateValue($event.target.value)" :value="value" type="email" class="input-value"/>
      <label class="input-span" for="email" :class="{ 'active': value }">{{ label }}</label>
      <div class="line"></div>
    </div>
    <div v-if="Type === 'password'" class="input-wrapper">
      <input v-on:input="updateValue($event.target.value)" :value="value" type="password" class="input-value"/>
      <label class="input-span" for="password" :class="{ 'active': value }">{{ label }}</label>
      <div class="line"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['label', 'value', 'Type'],
  data () {
    return {
      type: 'text'
    }
  },
  methods: {
    updateValue (value) {
      this.$emit('input', value)
    }
  }
}
</script>
<style lang="scss" scoped>
  .input-wrapper {
    display: flex;
    flex-direction: column;
    z-index: 3;
  }
  .input-value {
    z-index: 2;
  }
  .input-span {
    z-index: 0;
  }
</style>
