import api from '../libs/api'

const login = async (email, password) => {
  const { data } = await api.post('login', {
    email,
    password
  })
  return data
}

const singup = async (email, name, password) => {
  const { data } = await api.post('signup', {
    email,
    name,
    password
  })
  return data
}

export {
  login,
  singup
}
