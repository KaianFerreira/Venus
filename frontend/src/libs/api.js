import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8080/'
})

// later put interceptors here
export default api