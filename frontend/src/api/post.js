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

const update = async (id, description, link, title) => {
  const { data } = await api.put(`editPost/${id}`, {
    description,
    link,
    title
  })
  return data
}

const remove = async (id) => {
  const { data } = await api.delete(`deletePost/${id}`)
  return data
}

const getAllUser = async (usuario) => {
  const { data } = await api.get(`public/profile/${usuario}`)
  return data
}

const follow = async (usuario) => {
  const { data } = await api.get(`follow/${usuario}`)
  return data
}

const social = async () => {
  const { data } = await api.get('private/profile')
  return data
}

const upvote = async (idPost) => {
  const { data } = await api.get(`upvote/${idPost}`)
  return data
}

export {
  getAll,
  create,
  update,
  remove,
  getAllUser,
  follow,
  upvote,
  social
}
