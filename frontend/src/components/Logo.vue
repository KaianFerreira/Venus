<template>
  <div class="logo">
    V<div v-if="!minimize">enus</div>
  </div>
</template>
<script>
export default {
  props: ['minimize']
}
</script>
<style lang="scss" scoped>
  @import '../assets/_scss/variables.scss';
  .logo {
    display: flex;
    margin: 20px 0;
    color: #00CEF5;
    font-family: Satisfy;
    font-size: 3em;
    position: relative;
    z-index: 0;
  }
  @media screen and (min-width: $desktop-width) {
    .logo {
      font-size: 4em !important;
    }
  }
</style>
