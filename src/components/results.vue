<template>
    <div class="main container">
            <div class="row">
                <div class="col-sm-6 result">
                    <div v-if="searchWords == '' ">
                        <h3>すべての検索結果</h3>
                    </div>

                    <div v-else>
                        <h3>{{searchWords}}の検索結果</h3>
                    </div>

                    <div v-if="searchKamoku.length >= 100">
                        <p>{{searchKamoku.length}}件 上位100件まで表示</p>
                    </div>

                    <div v-else>
                        <p>{{searchKamoku.length}}件</p>
                    </div>
                    
                </div>
                <div class="col">
                    <div class="sort">

                        <button class="help_link__button" @click="openModal">
                            {{ selectedSort.label }}
                            <i class="material-icons">launch</i>
                        </button>

                        <selectModal v-if="modalFlag" @close-modal="closeModal">
                            <h2>表示順を変更</h2>

                            <div class="checkbox d-flex flex-wrap">
                                <div class="p-2 bd-highlight" v-for="(sort, s) in optionsSort" :key="s">
                                    <input :id="'sort' + s" type="radio" :value="sort" v-model="selectedSort">
                                    <label :for="'sort' + s"><span>{{ sort.label }}</span></label>
                                </div>
                            </div>

                            <button class="closebtn" @click="closeModal">
                                閉じる
                                <i class="material-icons">close</i>
                            </button>
                        </selectModal>

                    </div>
                </div>
            </div>
            
                <div class="table-box" v-for="(value, index) in sorted.slice(0,100)" :key="index" >
                    <div class="container">
                        <div class="row">
                            <div class="col-sm-12 col-md-2">{{index+1}}.  {{value.kamoku}} </div>
                            <div class="col-sm-12 col-md-2 gakubu">{{value.gakubu}} <br class="pc">{{value.gakka}}</div>
                            <div class="col-sm-4 col-md-2"> {{value.tantou}}</div>
                            <div class="col-sm-4 col-md-2">{{value.kyoushitsu}}</div>
                            <div class="col-sm-4 col-md-2">{{value.gakki}} <br>{{value.niti}}曜 {{value.gen}}限</div>
                            <div class="col-sm-12">{{value.bikou}}</div>
                        </div>
                    </div>
                </div>

                <!-- 300件以上 エラー -->
                <div class="error-too-long" v-if="searchKamoku.length >= 300">
                    <img src="~/assets/img/error.png">
                    <h2>あい!データが100件以上あるわけよ。<br>
                        こんな沢山あったらあわてぃはーてぃーするから
                        条件絞ろうね〜</h2>
                </div>

                <!-- 0件　エラー -->
                <div class="error-too-long" v-if="searchKamoku.length == 0">
                    <img src="~/assets/img/error.png">
                    <h2>おっと...「{{searchWords}}」は見つからなかったみたいだ...</h2>
                </div>

    </div>
</template>


<script>
import { mapState } from "vuex";
import selectModal from '@/components/selectModal.vue'
import lists from '@/assets/list-2.json'

export default {

    components: {
        selectModal
    },

    data() {
        return {
            modalFlag: false,

            optionsSort: [
                {"label":"科目名順", "code":"kamoku"},
                {"label":"教員名順", "code":"tantou"},
                {"label":"曜日順", "code":"niti"},
                {"label":"時限順", "code":"gen"}
            ],

            lists: lists,

            formResult: '',
            seasonResult: '',
            hourResult: '',
            daysResult: ''
        }
    },

    methods: {
        openModal() {
            this.modalFlag = true
        },
        closeModal() {
            this.modalFlag = false
        }
    },

    computed: {
        ...mapState([
            "searchWords","selectedSeason","selectedForm","selectedDays","selectedTimes","selectedSort"
        ]),

        selectedSort: {
            get: function() {
                return this.$store.state.selectedSort;
            },
            set: function(sort) {
                this.$store.commit('setSort', sort)
            }
        },
        
        replaceWords() {
            return this.searchWords.replace(/ /g, '　');
        },

        sorted() {
            if (this.selectedSort === null || this.selectedSort.code == 'kamoku') {
                return this.searchKamoku.sort((a, b) => {
                    return a.kamoku.localeCompare(b.kamoku, 'ja');
                });

            } else if (this.selectedSort.code == 'tantou'){
                return this.searchKamoku.sort((a, b) => {
                    return a.tantou.localeCompare(b.tantou, 'ja');
                });

            } else if (this.selectedSort.code == 'niti'){
                const daysOrder = ['月', '火', '水', '木', '金', '土', '日'];
                return this.searchKamoku.sort((a, b) => {
                    return daysOrder.indexOf(a.niti) - daysOrder.indexOf(b.niti);
                });

            } else if (this.selectedSort.code == 'gen'){
                return this.searchKamoku.sort((a, b) => {
                    return a.gen.localeCompare(b.gen, 'ja');
                });
            }
        },

        searchKamoku() {
            return this.lists.filter(value => {

                if (this.selectedForm == "online") {
                    this.formResult = value.kyoushitsu.match('^(?=.*ｵﾝﾗｲﾝ授業).*$')
                } else if (this.selectedForm == "real") {
                    this.formResult = value.kyoushitsu.match('^(?!.*ｵﾝﾗｲﾝ授業).*$')
                } else {
                    this.formResult = value.kyoushitsu.match('(?=.)')
                }

                if (this.selectedSeason == "season0") {
                    this.seasonResult = value.gakki.match('^(?=.*通年).*$')
                } else if (this.selectedSeason == "season1") {
                    this.seasonResult = value.gakki.match('^(?=.*前期).*$')
                } else if (this.selectedSeason == "season2") {
                    this.seasonResult = value.gakki.match('^(?=.*後期).*$')
                } else {
                    this.seasonResult = value.gakki.match('(?=.)')
                }

                if (this.selectedTimes && this.selectedTimes.length) {
                    this.hourResult = value.gen.match('[' + this.selectedTimes.join('') + ']')
                } else {
                    this.hourResult = value.gen.match('[1234567]')
                }

                if (this.selectedDays && this.selectedDays.length) {
                    this.daysResult = value.niti.match('[' + this.selectedDays.join('') + ']')
                } else {
                    this.daysResult = value.niti.match('[月火水木金土]')
                }

                return this.formResult && this.seasonResult &&
                    this.hourResult && this.daysResult &&
                    (value.kamoku.includes(this.searchWords) ||
                        value.gakubu.includes(this.searchWords) ||
                        value.gakka.includes(this.searchWords) ||
                        value.tantou.includes(this.searchWords))
            })
        }
    }

}
</script>


<style>
/*---------------------------------
  
  2.main    検索結果

---------------------------------*/

/* 検索結果 概要 */
.result { margin: auto 5%; }

/* 検索結果 ソート */
.sort { width: 170px; margin: 5% 10% 5% auto; }

.sort .vs__dropdown-toggle {
    width: 100%;
    margin: 10px 0 10px auto;
    padding: 0 0 5px 11px;
    border: 2px solid #2D2D2D;
    border-radius: 20px;
}

.sort #vs3__listbox {
    position: absolute;
    right: 0;
    width: 30%;
    margin: 10px 0 10px auto;
    padding: 0 0 5px 0;
    border-radius: 10px;
}

/* 検索結果テーブル */
.table-box {
    margin: 1% 4%;
    padding: 1%;
    border-radius: 15px;
    background-color: #F2F2F2;
}

/* エラー　件数が300以上 */
.error-too-long { margin: 5% 0; text-align: center; }

.error-too-long img { height: 150px; margin: 0 auto; }


/* タブレット　*/ 

@media only screen and (max-width: 766px) {

/* 検索結果 概要 */
.result { margin: auto 0 auto 4%; }

/* 検索結果 ソート */
.sort { width: 170px; margin: 10% 7% 10% auto; }

/* 検索結果テーブル */
.table-box { margin: 2% 4%; padding: 2% 1%; }

/* 検索結果　テーブル　学部学科 */
.gakubu { margin: 10px 0; }

}


/* スマホ用 */

@media only screen and (max-width: 575px) {

/* 検索結果 概要 */
.result { margin: 5% 4% 0 4%; }

/* 検索結果 ソート */
.sort { width: 170px; margin: 5% 5% 5% auto; }

/* 検索結果テーブル */
.table-box { margin: 3% 4%; padding: 2% 1%; }

}
</style>