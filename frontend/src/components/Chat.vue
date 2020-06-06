<template>
  <div>
    <p v-if="isConnected">We're connected to the server!</p>
    <div v-for="msg in messages" :key="msg">
        <h1>{{ msg.author }} : {{ msg.message }} </h1>
    </div>
    <br>
    <br>
    <Input :return="inputMessage" label='Message' Type='text'/>
    <button @click="sendMessage()">Enviar</button>
  </div>
</template>

<script>
import io from 'socket.io-client'

export default {
  data () {
    return {
      isConnected: false,
      socketMessage: '',
      messageObj: {},
      messages: [],
      socket: null
    }
  },
  mounted () {
    this.socket.on('receivedMessage', (message) => {
      this.messages.push(message)
    })
  },
  created () {
    this.socket = io('http://localhost:3333')
  },
  methods: {
    inputMessage (value) {
      this.messageObj.message = value
    },
    sendMessage () {
      // Send the "pingServer" event to the server.
      this.messageObj.author = 'teste'
      this.socket.emit('sendMessage', this.messageObj)
      this.messages.push(this.messageObj)
      console.log(this.$socket)
    }
  }
}
</script>
