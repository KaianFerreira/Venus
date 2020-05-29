import api from './api'

const SESSION_NAME = 'venusSession'

const getToken = () => {
  const token = JSON.parse(localStorage.getItem(SESSION_NAME))
  if (token) api.defaults.headers.Authorization = `Bearer ${token}`
}

const setToken = (token) => {
  api.defaults.headers.Authorization = `Bearer ${token}`
  localStorage.setItem(SESSION_NAME, JSON.stringify(token))
}

const removeToken = () => {
  delete api.defaults.headers.Authorization
  localStorage.removeItem(SESSION_NAME)
}

export {
  getToken,
  setToken,
  removeToken
}