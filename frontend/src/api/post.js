import api from '../libs/api'

const getAll = async () => {
  const { data } = await api.get('posts')
  return data
}

const create = async (description, link, title) => {
    const { data } = await api.post('post', {
        description,
        link,
        title
    })
    return data
  }

const getAllUser = async (usuario) => {
    const { data } = await api.get(`public/profile/${usuario}`)
    return data
  }

  export {
    getAll,
    create,
    getAllUser
  }