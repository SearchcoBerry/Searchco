export const state = () => ({
    searchWords: '',

    selectedSeason: 'seasonall',
    selectedForm: " ",
    selectedDays: [],
    selectedTimes: [],
    selectedSort: {"label":"科目名順", "code":"kamoku"}
})

export const mutations = {
    // @input 検索ワード取得
    setWords (state, msg) {
        state.searchWords = msg;
    },

    //@Click 学期
    setSeason (state, value) {
        state.selectedSeason = value;
    },

    //@Click 授業形態
    setForm (state, value) {
        state.selectedForm = value;
    },

    //@Click 曜日
    setDays (state, value) {
        state.selectedDays = value;
    },

    //@Click 時限
    setTimes(state, value) {
        state.selectedTimes = value;
    },

    //@Click 表示順
    setSort (state, value) {
        state.selectedSort = value;
    },
}

