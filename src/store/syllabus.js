export const state = () => ({
    syllabusData: []
})

export const mutations = {
  setSyllabus(state, value) {
    state.syllabusData = value; 
  }
}