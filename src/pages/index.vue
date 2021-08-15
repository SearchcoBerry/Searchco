<template>
    <div id="app">

        <div class="header">
            <div class="jumbotron">
                <div class="container">
                    <div class="row">
                        <div class="col-md-6 order-md-2 top-message">

                            <h1>あなたの履修登録に<br>幸子あれ</h1>

                            <p>
                                ※時間割データは2021年度前期・後期・通年分です。<br>
                                　(取得日: 2021年7月24日)<br>
                                ※時間割は変更の可能性があります。<br>
                                　学内の掲示板又は沖国大ポータルで最新の情報を確認して下さい。
                            </p>
                        </div>

                        <div class="col-md-6 order-md-1 top-search">
                                <div class="search-box">
                                    <h3>講義を探す</h3>
                                    <div class="search-form">
                                        <input type="text" v-model="searchWords" placeholder="科目名 教員名 学部学科 etc.">
                                        <i class="material-icons">search</i>
                                    </div>
                                </div>
                                
                                <div class="search-conditions">
                                    <h3>条件を絞る</h3>
                                    <!-- 学期 -->
                                    <div class="semester">
                                        <input type="radio" id="s_one" value="seasonall" v-model="season">
                                        <label for="s_one"><span>すべての学期</span></label>

                                        <br class="sp">

                                        <input type="radio" id="s_two" value="season0" v-model="season">
                                        <label for="s_two"><span>通年</span></label>

                                        <input type="radio" id="s_three" value="season1" v-model="season">
                                        <label for="s_three"><span>前期</span></label>

                                        <input type="radio" id="s_four" value="season2" v-model="season">
                                        <label for="s_four"><span>後期</span></label>
                                        
                                    </div>
                                    
                                    <!-- 授業形態 -->
                                    <div class="class-style">
                                        <input type="radio" id="f_one" value=" " v-model="form">
                                        <label for="f_one"><span>すべての授業形態</span></label>

                                        <br class="sp">

                                        <input type="radio" id="f_two" value="real" v-model="form">
                                        <label for="f_two"><span>対面</span></label>

                                        <input type="radio" id="f_three" value="online" v-model="form">
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

                                    
                                    <selectModal v-if="modalPeriod" @close-modal="closeModalPeriod">
                                        <h2>時期を指定</h2>

                                        <div class="checkbox row">
                                            <h3>曜日</h3> 
                                            <div class="col" v-for="(day, d) in optionsDays" :key="d">
                                                <input :id="'day' + d" type="checkbox" :value="day" v-model="selectedDays">
                                                <label :for="'day' + d">  <span>{{ day }}曜</span>  </label>
                                            </div>
                                        </div>

                                        <div class="checkbox row">
                                            <h3>時限</h3> 
                                            <div class="col" v-for="(time, t) in optionsTimes" :key="t">
                                                <input :id="'time' + t" type="checkbox" :value="time" v-model="selectedTimes">
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
                    </div>
                    
                </div>
            </div>
        </div>

        <div class="main container">
            <div class="row">
                <div class="col-sm-6 result">
                    <div v-if="searchWords == '' ">
                        <h3>すべての検索結果</h3>
                    </div>

                    <div v-else>
                        <h3>{{searchWords}}の検索結果</h3>
                    </div>

                    <div v-if="searchKamoku.length >= 300">
                        <p>{{searchKamoku.length}}件 上位200件まで表示</p>
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

                            <div class="checkbox row">
                                <div class="col-md-6" v-for="(sort, s) in optionsSort" :key="s">
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
            
                <div class="table-box" v-for="(value, index) in sorted.slice(0,200)" :key="index" >
                    <div class="container">
                        <div class="row">
                            <div class="col-md-2">{{index+1}}.  {{value.kamoku}} </div>
                            <div class="col-md-2 gakubu">{{value.gakubu}} <br class="pc">{{value.gakka}}</div>
                            <div class="col-md-2 col-sm-4"> {{value.tantou}}</div>
                            <div class="col-md-2 col-sm-4">{{value.kyoushitsu}}</div>
                            <div class="col-md-2 col-sm-4">{{value.gakki}} <br>{{value.niti}}曜 {{value.gen}}限</div>
                            <div class="col-md-2">{{value.bikou}}</div>
                        </div>
                    </div>
                </div>

                <!-- 300件以上 エラー -->
                <div class="error-too-long" v-if="searchKamoku.length >= 300">
                    <img src="~/assets/img/error.png">
                    <h2>あい!データが200件以上あるわけよ。<br>
                        こんな沢山あったらあわてぃはーてぃーするから
                        条件絞ろうね〜</h2>
                </div>

                <!-- 0件　エラー -->
                <div class="error-too-long" v-if="searchKamoku.length == 0">
                    <img src="~/assets/img/error.png">
                    <h2>おっと...「{{searchWords}}」は見つからなかったみたいだ...</h2>
                </div>

        </div>


        
    </div>
</template>

<script>
import lists from '@/assets/list-2.json'
import selectModal from '@/components/selectModal.vue'

export default {
    components: {
        selectModal
    },

    data: () => ({
        modalPeriod: false,
        modalFlag: false,

        optionsDays: ["月","火","水","木","金","土"],
        optionsTimes: ["1","2","3","4","5","6","7"],
        optionsSort: [
            {"label":"科目名順", "code":"kamoku"},
            {"label":"教員名順", "code":"tantou"},
            {"label":"曜日順", "code":"niti"},
            {"label":"時限順", "code":"gen"}
            ],

        searchWords: '',
        lists: lists,

        season: 'seasonall',
        selectedDays: [],
        selectedTimes: [],
        selectedSort: {"label":"科目名順", "code":"kamoku"},

        form: " ",

        formResult: '',
        seasonResult: '',
        hourResult: '',
        daysResult: '',
    }),

    methods: {
        openModalPeriod() {
            this.modalPeriod = true
        },
        closeModalPeriod() {
            this.modalPeriod = false
        },
        openModal() {
            this.modalFlag = true
        },
        closeModal() {
            this.modalFlag = false
        }
    },


    computed: {

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

                if (this.form == "online") {
                    this.formResult = value.kyoushitsu.match('^(?=.*ｵﾝﾗｲﾝ授業).*$')
                } else if (this.form == "real") {
                    this.formResult = value.kyoushitsu.match('^(?!.*ｵﾝﾗｲﾝ授業).*$')
                } else {
                    this.formResult = value.kyoushitsu.match('(?=.)')
                }

                if (this.season == "season0") {
                    this.seasonResult = value.gakki.match('^(?=.*通年).*$')
                } else if (this.season == "season1") {
                    this.seasonResult = value.gakki.match('^(?=.*前期).*$')
                } else if (this.season == "season2") {
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
                        value.tantou.includes(this.replaceWords))
            })
        }
    }
        

}
</script>


<style>

/*---------------------------------
  
  1.header  検索フォーム・メッセージ
    1.背景
    2.メッセージ
    3.検索フォーム

  2.main    検索結果
    1.検索結果 概要
    2.ソート選択
    3.テーブル
    4.エラー表示

  3.mb      スマホ・タブレットcss
    1.タブレット
    2.スマホ

---------------------------------*/



/* モーダルコンポーネント ボタン*/
.checkbox {
    padding-bottom: 20px;
    line-height: 3em;
}


.help_link__button {
    position: relative;
    text-align: left;
    background-color: #FFF;
    padding: 8px 20px;
    border-radius: 100px;
    border: 2px solid;
    border-color: #2D2D2D;
    width: 100%;
    margin: 1% 0;
}


.help_link__button i {
  position: absolute;
  top: 3px;
  right:20px;
  color: #2D2D2D;
}

.closebtn {
    position: relative;
    text-align: left;
    background-color: #FFF;
    padding: 8px 20px;
    border-radius: 100px;
    border: 2px solid;
    border-color: #2D2D2D;
    width: 150px;
    margin: 1% 0;
}

.closebtn i {
  position: absolute;
  top: 3px;
  right:15px;
  color: #2D2D2D;
}

/*---------------------------------
  
  1.header  検索フォーム・メッセージ

---------------------------------*/

.jumbotron {
    background:url(~/assets/img/background-img.png)
    center no-repeat; 
    background-size: cover;
}

/* トップメッセージ */
.top-message {
    margin: auto 0;
    padding: 50px 0 ;
}
.top-message h1 {
    font-weight: 700;
}
.top-message p {
    margin-top: 20px;
    font-size: 15px;
    color: #868686;
}

/* 検索枠 */
.top-search {
    width: 40%;
    margin: 5%;
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

.search-form input[type=text]:focus {
	border-color: #FFA100;
}
.search-form input[type=text] {
	padding-left: 50px;
}

.search-form ::placeholder {
  color: #EEE;
}

.search-form i {
	position: absolute;
	top: 10px;
	left: 0;
	padding: 11px 15px;
	transition: 0.3s;
	color: #FFF;
}




/* 条件を絞る */
.search-conditions {
    margin: 10px 0;
}

.search-conditions span{
    display: inline-block;
}

.semester, .class-style {
    margin-bottom: 0;

    line-height: 3em;
}

/* ラジオボタン */

input[type=radio] {
display: none; /* ラジオボタンを非表示にする */
}

input[type=checkbox] {
display: none; /* ラジオボタンを非表示にする */
}

label {
  background-color: none;
  padding: 8px 20px;
  border-radius: 100px;
  border: 2px solid;
  border-color: #2D2D2D;
}

input[type=radio]:checked + label {
  background-color: #FFA100;
  color: #fff;
  border:1px solid;
  border-color: #FFA100;
}

input[type=checkbox]:checked + label {
  background-color: #FFA100;
  color: #fff;
  border:1px solid;
  border-color: #FFA100;
}


/* 曜日・時限モーダル */




/*---------------------------------
  
  2.main    検索結果

---------------------------------*/

/* 検索結果 概要 */
.result {
    margin: auto 5%;
}

/* 検索結果 ソート */
.sort {
    width: 170px;
    margin: 5% 10% 5% auto;
}
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
.error-too-long {
    margin: 5% 0;
    text-align: center;
}
.error-too-long img {
    height: 150px;
    margin: 0 auto;
}




/*---------------------------------
  
  3.mb      スマホ・タブレットcss

---------------------------------*/

/* パソコンで見たときは"pc"のclassがついたコンテンツを表示 */
.pc { display: block !important; }
.sp { display: none !important; }
 
/* スマートフォンで見たときは"sp"のclassがついたコンテンツを表示 */
@media only screen and (max-width: 766px) {
    .pc { display: none !important; }
    .sp { display: block !important; }
}


/* タブレット　*/ 

@media only screen and (max-width: 766px) {

/* 背景を変更 */
.jumbotron {
    background:url(~/assets/img/mb-background.png)
    center repeat; 
    background-size: 300%;
}

/* トップメッセージ */
.top-message {
    padding: 50px 4%;
}

/* 検索枠 */
.top-search {
    width: 90%;
}

/* 検索結果 概要 */
.result {
    margin: auto 0 auto 4%;
}

/* 検索結果 ソート */
.sort {
    width: 170px;
    margin: 10% 7% 10% auto;
}

/* 検索結果テーブル */
.table-box {
    margin: 2% 4%;
    padding: 2% 1%;
}

/* 検索結果　テーブル　学部学科 */
.gakubu {
    margin: 10px 0;
}

}


/* スマホ用 */

@media only screen and (max-width: 575px) {

/* トップメッセージ */
.top-message {
    padding: 50px 4%;
}

/* 検索結果 概要 */
.result {
    margin: 5% 4% 0 4%;
}

/* 検索結果 ソート */
.sort {
    width: 170px;
    margin: 5% 5% 5% auto;
}

/* 検索結果テーブル */
.table-box {
    margin: 3% 4%;
    padding: 2% 1%;
}

}

</style>