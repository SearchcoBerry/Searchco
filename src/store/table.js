export const strict = false 
export const state = () => ({

    favorite: []
})

export const mutations = {
  setFavorite(state, value) {
    state.favorite = value; 
  }
}

export const getters = {
  timeTable(state) {
    return state.favorite;
  }
}
