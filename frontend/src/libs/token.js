import api from './api'

const SESSION_NAME = 'venusSession'

const getData = () => {
  const data = JSON.parse(localStorage.getItem(SESSION_NAME))
  return data
}

const setData = (data) => {
  localStorage.setItem(SESSION_NAME, JSON.stringify(data))
  api.defaults.headers.Authorization = data.token
}

// const setApiHeaders = (token) => {
//   api.defaults.headers.Authorization = token
// }

const removeData = () => {
  delete api.defaults.headers.Authorization
  localStorage.removeItem(SESSION_NAME)
  return null
}

export {
  getData,
  setData,
  // setApiHeaders,
  removeData
}
