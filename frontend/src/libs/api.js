import axios from 'axios'
import { removeData } from './token'
import router from '../router'
const api = axios.create({
  baseURL: 'http://localhost:3000/'
})
// later put interceptors here

api.interceptors.response.use(undefined, error => {
  if (error.response.status === 401) {
    removeData()
    router.push('/signin')
    return null
  }
  return Promise.reject(error)
})
export default api
