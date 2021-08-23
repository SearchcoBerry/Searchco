export const strict = false 
export const state = () => ({

    favorite: []
})

export const mutations = {
  setFavorite(state, value) {
    const daysOrder = ['月', '火', '水', '木', '金', '土'];
    //const days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat'];
    
    // value = daysOrder.indexOf(a.niti) - daysOrder.indexOf(b.niti) || a.gen.localeCompare(b.gen, 'ja');
    //const myKey = daysOrder.indexOf(value.niti);
    //const obj = {[myKey]: value.kamoku};
    
    //state.table.splice(value.gen, 1, obj);

    value.sort((a, b) => {
      return a.gen - b.gen  ||  daysOrder.indexOf(a.niti) - daysOrder.indexOf(b.niti);
     });

    state.favorite = value; 
  }
}

export const getters = {
  timeTable(state) {
    return state.favorite;
  }
}
