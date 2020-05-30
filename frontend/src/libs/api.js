import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:3000/'
})
// later put interceptors here
export default api
