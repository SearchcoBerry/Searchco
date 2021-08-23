<template>
    
    <div class="top-search">
        <div class="search-box">
            <h3>講義を探す</h3>
            <div class="search-form">
                <input type="text" placeholder="科目名 教員名 学部学科 etc."  @input="setWords">
                <i class="material-icons">search</i>
            </div>
        </div>
        
        <div class="search-conditions">
            <h3>条件を絞る</h3>
            <!-- 学期 -->
            <div class="semester">
                <input type="radio" id="s_one" value="seasonall" v-model="setSeason">
                <label for="s_one"><span>すべての学期</span></label>

                <br class="sp">

                <input type="radio" id="s_two" value="season0" v-model="setSeason">
                <label for="s_two"><span>通年</span></label>

                <input type="radio" id="s_three" value="season1" v-model="setSeason">
                <label for="s_three"><span>前期</span></label>

                <input type="radio" id="s_four" value="season2" v-model="setSeason">
                <label for="s_four"><span>後期</span></label>
                
            </div>
            
            <!-- 授業形態 -->
            <div class="class-style">
                <input type="radio" id="f_one" value=" " v-model="setForm">
                <label for="f_one"><span>すべての授業形態</span></label>

                <br class="sp">

                <input type="radio" id="f_two" value="real" v-model="setForm">
                <label for="f_two"><span>対面</span></label>

                <input type="radio" id="f_three" value="online" v-model="setForm">
                <label for="f_three"><span>オンライン</span></label>
            </div> 


            <!-- 時期を指定  -->
            <button class="help_link__button" @click="openModalPeriod">
                <div v-if="selectedDays.length == 0 && selectedTimes.length == 0">
                    すべての曜日・時限
                    <i class="material-icons">launch</i>
                </div>

                <div v-else-if="selectedDays.length == 0 && selectedTimes.length != 0">
                    すべての曜日　時限: {{ selectedTimes.join(',') }}
                    <i class="material-icons">launch</i>
                </div>

                <div v-else-if="selectedDays.length != 0 && selectedTimes.length == 0">
                    曜日: {{ selectedDays.join(',') }}　すべての時限
                    <i class="material-icons">launch</i>
                </div>

                <div v-else>
                    曜日: {{ selectedDays.join(',') }}　時限: {{ selectedTimes.join(',') }}
                    <i class="material-icons">launch</i>
                </div>

            </button>

            <!-- モーダル　コンポーネント　呼び出し -->
            <selectModal v-if="modalPeriod" @close-modal="closeModalPeriod">
                <h2>時期を指定</h2>

                <h3>曜日</h3> 
                <div class="checkbox d-flex flex-wrap">
                    <div class="p-1 bd-highlight" v-for="(day, d) in optionsDays" :key="d">
                        <input :id="'day' + d" type="checkbox" :value="day"  v-model="selectedDays">
                        <label :for="'day' + d">  <span>{{ day }}曜</span>  </label>
                    </div>
                </div>

                <h3>時限</h3> 
                <div class="checkbox d-flex flex-wrap">
                    <div class="p-1 bd-highlight" v-for="(time, t) in optionsTimes" :key="t">
                        <input :id="'time' + t" type="checkbox" :value="time"  v-model="selectedTimes">
                        <label :for="'time' + t">  <span>{{ time }}限</span>  </label>
                    </div>
                </div>
                
                <button class="closebtn" @click="closeModalPeriod">
                    閉じる
                    <i class="material-icons">close</i>
                </button>
            </selectModal>
            
        </div>


    </div>

</template>

<script>
import { mapState } from "vuex";
import results from '~/components/results.vue'
export default {
    data() {
        return {
            modalPeriod: false,

            optionsDays: ["月","火","水","木","金","土"],
            optionsTimes: ["1","2","3","4","5","6","7"],
        }
    },

    computed:{
        ...mapState([
            "searchWords","selectedSeason","selectedForm","selectedDays","selectedTimes","selectedSort"
        ]),

        setSeason: {
            get: function() {
                return this.$store.state.selectedSeason;
            },
            set: function(season) {
                this.$store.commit('setSeason', season)
            }
        },
        setForm: {
            get: function() {
                return this.$store.state.selectedForm;
            },
            set: function(form) {
                this.$store.commit('setForm', form)
            }
        },
        selectedDays: {
            get: function() {
                return this.$store.state.selectedDays;
            },
            set: function(day) {
                this.$store.commit('setDays', day)
            }
        },
        
        selectedTimes: {
            get: function() {
                return this.$store.state.selectedTimes;
            },
            set: function(time) {
                this.$store.commit('setTimes', time)
            }
        }
        

    },

    mounted: function() {
        this.$store.commit('setSeason', 'seasonall'),
        this.$store.commit('setForm', ' ')
    },

    methods: {
        openModalPeriod() {
            this.modalPeriod = true
        },
        closeModalPeriod() {
            this.modalPeriod = false
        },

        setWords(e) {
            this.$store.commit('setWords', e.target.value)
        }
    },

    components: {
        results
    },
    
}
</script>

<style>
/*---------------------------------
  
  1.header  検索フォーム・メッセージ

---------------------------------*/

/* 検索枠 */
.top-search {
    width: 80%;
    margin: 8%;
    padding: 30px;
    background-color: #FFF;
    border-radius: 20px;
}

/* 入力フォーム */
.search-form {
    position: relative;
	width: 100%;
	margin: 3% 0;
}

.search-form input[type=text] {
	box-sizing: border-box;
	width: 100%;
	margin: 10px 0;
	padding: 0.7em;
	transition: 0.3s;
    color: #FFF;
	background-color: #868686;
    border: none;
	border-radius: 30px;
	outline: none;
}

.search-form input[type=text]:focus { border-color: #FFA100; }

.search-form input[type=text] { padding-left: 50px; }

.search-form ::placeholder { color: #EEE; }

.search-form i {
	position: absolute;
	top: 10px;
	left: 0;
	padding: 11px 15px;
	transition: 0.3s;
	color: #FFF;
}


/* 条件を絞る */
.search-conditions { margin: 10px 0; }

.search-conditions span{ display: inline-block; }

.semester, .class-style {
    width: 100%;
    margin-bottom: 0;
    line-height: 2.5em;
}

/* ラジオボタン */

input[type=radio] { display: none; }/* ラジオボタンを非表示にする */

input[type=checkbox] { display: none;} /* ラジオボタンを非表示にする */ 

.top-search label {
  display: inline-block;
  background-color: #FFF;
  margin: 1% 0;
  padding: 0 20px;
  border-radius: 100px;
  border: 2px solid;
  border-color: #2D2D2D;
}

.top-search input[type=radio]:checked + label {
  background-color: #FFA100;
  color: #fff;
  border:1px solid;
  border-color: #FFA100;
}

.top-search input[type=checkbox]:checked + label {
  background-color: #FFA100;
  color: #fff;
  border:1px solid;
  border-color: #FFA100;
}

/* タブレット　*/ 

@media only screen and (max-width: 766px) {
    .top-search {
        width: 90%;
        margin: 2.5%;
    }
}

/* スマホ用 */
@media only screen and (max-width: 575px) {
    .top-search {
        width: 95%;
        margin: 0 2.5% 10% 2.5%;
    }
}

</style>