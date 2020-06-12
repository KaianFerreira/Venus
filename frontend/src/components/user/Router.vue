<template>
  <div class="menu-container">
    <div class="menu" :class="{ 'close' : closed }">
      <div class="header">
        <Logo :minimize="closed"/>
      </div>
      <div class="content">
        <div class="user">
          <div class="photo">
            <IconPerson css="icon-user"/>
          </div>
          <div class="name" @click="$router.push(`/profile/${user.name}`)">
            {{ user.name.split(' ')[0] }}
          </div>
          <div class="actions">
            <div class="icon-wrapper" @click="signOut">
              <IconLogOut css="icon"/>
            </div>
          </div>
        </div>
        <div class="wrapper"  @click="$router.push('/')">
          <div class="menu-item">
            <div class="icon-wrapper">
              <IconHome css="icon"/>
            </div>
            <span class="title">Home</span>
          </div>
        </div>
        <div class="wrapper">
          <div class="menu-item">
            <span class="title">Pessoas que você segue:</span>
          </div>
        </div>
        <div v-for="followed in following" :key="followed.id">
          <div class="wrapper" @click="$router.push(`/profile/${followed.followed}`)">
            <div class="icon-wrapper">
              <IconPerson css="icon"/>
            </div>
            <div class="menu-item">
              <span class="title">{{ followed.followed }}</span>
            </div>
          </div>
        </div>
        <div class="wrapper">
          <div class="menu-item">
            <span class="title">Pessoas que seguem você:</span>
          </div>
        </div>
        <div v-for="follower in followers" :key="follower.id">
          <div class="wrapper">
            <div class="icon-wrapper">
              <IconPerson css="icon"/>
            </div>
            <div class="menu-item">
              <span class="title">{{ follower.followed }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="footer">
        <div class="icon-wrapper" @click="closed = !closed">
          <IconArrow :css="closed ? 'icon' : 'icon rotate'"/>
        </div>
      </div>
    </div>
    <router-view class="router-view" :class="{ 'close': closed }"/>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { social } from '../../api/post'
export default {
  computed: {
    ...mapState(['user'])
  },
  data () {
    return {
      closed: true,
      followers: [],
      following: []
    }
  },
  mounted () {
    this.social()
  },
  methods: {
    signOut () {
      this.$store.dispatch('signOut')
    },
    async social () {
      try {
        this.error = null
        const res = await social()
        if (!res.Sucess) this.error = res.Cause
        this.followers = res.followers
        this.following = res.following
        console.log(this.following)
      } catch (error) {
        console.log(new Error(error))
        console.log('Deu erro')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
  @import '../../assets/_scss/variables.scss';
  .menu-container {
    display: flex;
    height: 100vh;
    width: 100%;
    .router-view {
      transition: 0.33s;
      flex-grow: 1;
      margin-left: 70px;
    }
    .menu {
      color: #fff;
      transition: 0.33s;
      padding: 10px;
      display:flex;
      flex-direction: column;
      background-color: $primary-color;
      position: fixed;
      width: calc(100% - 20px);
      height: calc(100% - 20px);
      z-index: 1;
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
        margin-top: 50px;
        .wrapper {
          transition: 0.33s;
          display: flex;
          align-items: center;
          border-radius: 10px;
          &:hover {
            background-color: #0062ff;
          }
        }
        .menu-item {
          transition: 0.33s;
          display: flex;
          padding: 10px;
          margin: 0px 10px;
          width: calc(100% - 22px);
          align-items: center;
          border-radius: 10px;
          border: 1px solid transparent;
          cursor: pointer;
          .title {
            margin-left: 20px;
          }
          &:hover {
            transform: translateX(10px);
          }
        }
        .user {
          transition: 0.33s;
          display: flex;
          align-items: center;
          justify-content: space-between;
          border: 1px solid darkgray;
          border-radius: 10px;
          width: calc(100% - 22px);
          color: white;
          padding: 10px;
          margin-bottom: 50px;

          .photo {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 48px;
            height: 48px;
            border: 1px solid $secondary-color;
            background-image: ceil($number: 0);
            border-radius: 50px;
            .icon-user {
              fill: darkgray;
              width: 50px;
              height: 50px;
            }
          }
          .name {
            flex-grow: 1;
            margin-left: 20px;
          }
        }
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
    .name {
      cursor: pointer
    }
    .close {
      .content {
        .name, .actions {
          display: none;
          cursor: pointer
        }
        .user {
          border: none;
          padding: 0;
        }
        .wrapper {

          .menu-item {
            margin-left: 0px;
            &:hover {
              transform: translateX(0px);
            }
            .title {
              display: none;
            }
          }
        }
      }
      .footer .icon-wrapper {
        flex-grow: 0;
        align-self: center;
      }
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
