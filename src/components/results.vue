<template>
    <!------------------------------------

    # 検索結果が多い場合に画像を表示して要素を減らす

    ------------------------------------->
    <!-- 
        <div v-if="searchWords == '' " class="container">
        <div class="row hint">
            <img class="pc" src="~/assets/img/hint_pc.png">
            <img class="sp" src="~/assets/img/hint_mb.png">
        </div>
    </div>
    -->

    <div class="main">
            <div class="row">
                <!-- {{setSyllabus}} -->
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

                        <!-- モーダル コンポーネント　呼び出し -->
                        <button class="help_link__button" @click="openModal">
                            {{ selectedSort.label }}
                            <i class="material-icons">launch</i>
                        </button>

                        <!-- モーダル コンポーネント 表示 -->
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
            
            <!-- 検索結果を表示 -->
            <div class="table-box" v-for="(value, index) in sorted.slice(0,100)" :key="index" >
                <div class="container">
                    <div class="row">
                        <div class="col-sm-12 col-md-2">{{index+1}}.  {{value.kamoku}} </div>
                        <div class="col-sm-12 col-md-2 gakubu">{{value.gakubu}} <br class="pc">{{value.gakka}}</div>
                        <div class="col-sm-4 col-md-2"> {{value.tantou}}</div>
                        <div class="col-sm-4 col-md-1">{{value.kyoushitsu}}</div>
                        <div class="col-sm-4 col-md-2">{{value.gakki}}　{{value.niti}}{{value.gen}}　{{value.sou}}{{value.ji}}</div>
                        <div class="col-sm-12 col-md-2 d-flex align-items-center">{{value.bikou}}</div>
                        <div class="col-sm-12 col-md-1 d-flex align-items-center">
                            <input type="checkbox" :id="'value' + index" :value="value" v-model="setFavorite">
                            <label :for="'value' + index"> <i class="icon"></i> </label>
                            
                            <!-- <input type="checkbox" :id="'syllabusValue' + index" :value="value" v-model="setSyllabus">
                            <label :for="'syllabusValue' + index"><i class="material-icons">info_outline</i><br></label> -->
                            <!-- <i class="material-icons">info_outline</i>  -->
                        </div>
                        
                    </div>
                </div>
            </div>

            <!-- 300件以上 エラー -->
            <div class="error-too-long" v-if="searchKamoku.length >= 100">
                <img src="~/assets/img/error.webp">
                <h2>あい!データが100件以上あるわけよ。<br>
                    こんな沢山あったらあわてぃはーてぃーするから
                    条件絞ろうね〜</h2>
            </div>

            <!-- 0件　エラー -->
            <div class="error-too-long" v-if="searchKamoku.length == 0">
                <img src="~/assets/img/error.webp">
                <h2>おっと...「{{searchWords}}」は見つからなかったみたいだ...</h2>
            </div>

    </div>
</template>


<script>
import { mapState } from "vuex";
import selectModal from '@/components/selectModal.vue'
import lists from '@/assets/timetable-2023-03.json'

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

        setFavorite: {
            get: function() {
                return this.$store.state.table.favorite;
            },
            set: function(favo) {
                this.$store.commit('table/setFavorite', favo)
            }
        },

        setSyllabus: {
           get: function() {
                return this.$store.state.syllabus.syllabusData;
           },
           set: function(sValue) {
                this.$store.commit('syllabus/setSyllabus', sValue)
                const url = '/syllabus'
                window.open(url, '_blank')
           }
        },
        
        replaceWords() {
            return this.searchWords.replace(/ /g, '　');
        },

        sorted() {
            switch (this.selectedSort.code){

                default:
                case 'kamoku':  // 科目名順
                    return this.searchKamoku.sort((a, b) => {
                        return a.kamoku.localeCompare(b.kamoku, 'ja');
                    });
                    break;

                case 'tantou':  // 教員名順
                    return this.searchKamoku.sort((a, b) => {
                        return a.tantou.localeCompare(b.tantou, 'ja');
                    });
                    break;

                case 'niti':    // 曜日順
                    const daysOrder = ['月', '火', '水', '木', '金', '土', '日'];
                    return this.searchKamoku.sort((a, b) => {
                        return daysOrder.indexOf(a.niti) - daysOrder.indexOf(b.niti);
                    });
                    break;

                case 'gen':     //　 時限順
                    return this.searchKamoku.sort((a, b) => {
                        return a.gen.localeCompare(b.gen, 'ja');
                    });
                    break;
            }
        },

        searchKamoku() {
            return this.lists.filter(value => {

                //--- 授業形態　フィルター ---//
                const form = this.selectedForm;

                if (form == "online") { this.formResult = value.kyoushitsu.match('^(?=.*ｵﾝﾗｲﾝ授業).*$') } 

                else if (form == "real") { this.formResult = value.kyoushitsu.match('^(?!.*ｵﾝﾗｲﾝ授業).*$') } 

                else { this.formResult = value.kyoushitsu.match('(?=.)') }


                //--- 学期 フィルター ---//
                const season = this.selectedSeason;

                if (season == "season0") { this.seasonResult = value.gakki.match('^(?=.*通年).*$') } 

                else if (season == "season1") { this.seasonResult = value.gakki.match('^(?=.*前期).*$') }

                else if (season == "season2") { this.seasonResult = value.gakki.match('^(?=.*後期).*$') }

                else { this.seasonResult = value.gakki.match('(?=.)') }


                //--- 時限 フィルター ---//
                const times = this.selectedTimes;

                if (times && times.length) { this.hourResult = value.gen.match('[' + times.join('') + ']') } 

                else { this.hourResult = value.gen.match('[1234567]') }


                //--- 曜日 フィルター ---//
                const days = this.selectedDays;

                if (days && days.length) { this.daysResult = value.niti.match('[' + this.selectedDays.join('') + ']') } 

                else { this.daysResult = value.niti.match('[月火水木金土]')  }



                return this.formResult && this.seasonResult &&
                    this.hourResult && this.daysResult &&
                    (value.kamoku.includes(this.searchWords) ||
                        value.gakubu.includes(this.searchWords) ||
                        value.gakka.includes(this.searchWords) ||
                        value.tantou.includes(this.replaceWords))
            })
        }
    }

}
</script>


<style>
/*---------------------------------
  
  2.main    検索結果

---------------------------------*/

.hint {
    margin: 0 2%;
    width: auto;
    height: auto;
}

/* 検索結果 概要 */
.result { margin: auto 5%; }

/* 検索結果 ソート */
.sort {float: right; margin: 5% 10% 5% auto; }

/* 検索結果テーブル */
.table-box {
    margin: 1% 4%;
    padding: 1%;
    border-radius: 15px;
    background-color: #F2F2F2;
}

.table-box:last-child{
    margin: 1% 4% 10% 4%;
    padding: 1%;
    border-radius: 15px;
    background-color: #F2F2F2;
}

/* 検索結果テーブル アイコン */
/* ラジオボタン */

/* ラジオボタン非表示は search.vue 250行付近 */

/* 順番並べ替え */
.sort label {
    display: inline-block;
    background-color: #FFF;
    margin: 1% 0;
    padding: 0 20px;
    border-radius: 100px;
    border: 2px solid;
    border-color: #2D2D2D;
}

.sort input[type=radio]:checked + label {
  background-color: #FFA100;
  color: #fff;
  border:1px solid;
  border-color: #FFA100;
}

.sort input[type=checkbox]:checked + label {
  background-color: #FFA100;
  color: #fff;
  border:1px solid;
  border-color: #FFA100;
}

/* 気になるボタン */
.icon::before {
    content: '\e87e'; 
    font-family: 'Material Icons';
    font-style: normal;
    font-size: 24px;
    color: #2D2D2D;
    cursor: pointer;
}

.table-box input[type=checkbox]:checked ~ label .icon::before{
    content: '\e87d'; 
    font-family: 'Material Icons';
    font-style: normal;
    font-size: 24px;
    color: #FFA100;
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
