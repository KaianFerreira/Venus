<template>
  <div class="menu-container">
    <div class="menu" :class="{ 'close' : closed }">
      <div class="header">
        <Logo :minimize="closed"/>
      </div>
      <div class="content">
        <div class="user">
          <div class="photo"></div>
          <div class="name">
            {{ user.name.split(' ')[0] }}
          </div>
        </div>
      </div>
      <div class="footer">
        <div class="icon-wrapper" @click="closed = !closed">
          <IconArrow :css="closed ? 'icon' : 'icon rotate'"/>
        </div>
      </div>
    </div>
    <router-view class="router-view"></router-view>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  computed: {
    ...mapState(['user'])
  },
  data () {
    return {
      closed: true
    }
  }
}
</script>

<style lang="scss" scoped>
  @import '../../assets/_scss/variables.scss';
  .menu-container {
    display: flex;
    height: 100vh;
    .menu {
      transition: 0.33s;
      padding: 10px;
      display:flex;
      flex-direction: column;
      background-color: $primary-color;
      width: 100%;
      &.close {
        width: 50px !important;
      }
      .header {
        display: flex;
        .logo {
          margin: 0;
          flex-grow: 1;
          display: flex;
          justify-content: center;
        }
      }
      .content {
        display: flex;
        flex-direction: column;
        width: 100%;
        flex-grow: 1;
      }
      .footer {
        width: 100%;
        display: flex;
        align-items: center;
        .icon-wrapper {
          justify-content: flex-end;
          margin: 10px;
          width: 100%;
        }
      }
    }
    .close .footer .icon-wrapper {
      flex-grow: 0;
      align-self: center;
    }
  }
  @media screen and (min-width: $desktop-width) {
    .menu {
      width: 350px !important;
      &.close {
        width: 60px !important;
      }
    }
  }
</style>
