// import api from './api'

const SESSION_NAME = 'venusSession'

const getToken = () => {
  const token = JSON.parse(localStorage.getItem(SESSION_NAME))
  return token
}

const setToken = (token) => {
  localStorage.setItem(SESSION_NAME, JSON.stringify(token))
}

const removeToken = () => {
  // delete api.defaults.headers.Authorization
  // localStorage.removeItem(SESSION_NAME)
  return null
}

export {
  getToken,
  setToken,
  removeToken
}
