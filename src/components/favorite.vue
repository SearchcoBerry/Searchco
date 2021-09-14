<template>
    <div class="favorite">
        <div class="row">
            
                <div class="col-sm-6 result">
                    <h3>"仮"時間割表</h3>
                    <p>{{pass}}</p>
                </div>

                <div class="col">
                    <div class="sort">

                        <!-- DBに保存 モーダル 呼び出し -->
                        <button class="help_link__button" @click="saveHandler" v-show="setFavorite.length">
                            保存する
                            <i class="material-icons">cloud_upload</i>
                        </button>

                        <!-- DBから読み込み モーダル コンポーネント　呼び出し -->
                        <button class="help_link__button" @click="loadOpenModal">
                            読み込む
                            <i class="material-icons">cloud_download</i>
                        </button>

                        <!-- DBに保存  表示 -->
                        <selectModal v-if="modalFlagSave" @close-modal="saveCloseModal">
                            <h2>時間割を保存しました</h2>

                            <p>合い言葉は…</p>
                            <h2>{{pass}}</h2>
                            <p>です。<br><br>保存期間:１ヶ月 </p>
                            
                            <button class="closebtn" @click="saveCloseModal">
                                閉じる
                                <i class="material-icons">close</i>
                            </button>
                        </selectModal>

                        <!-- DBから読み込み  表示 -->
                        <selectModal v-if="modalFlagLoad" @close-modal="loadCloseModal">
                            <h2>時間割を読み込む</h2>

                            <p>合い言葉を入力してください</p>
                            <div class="search-form">
                                <input type="text" v-model="pass">
                                <i class="material-icons">lock_open</i>
                            </div>

                            <button class="closebtn" @click="loadCloseModal">
                                キャンセル
                                <i class="material-icons">close</i>
                            </button>

                            <button class="closebtn done" @click="loadHandler">
                                読み込む
                                <i class="material-icons">done</i>
                            </button>
                            
                            
                        </selectModal>

                        <!-- 読み込み失敗  表示 -->
                        <selectModal v-if="modalFlagError" @close-modal="errorCloseModal">
                            <h2>読み込みに失敗…</h2>
                            <p>合い言葉が一致しませんでした。<br>なーいちどぅう試しくぃみそーれー</p>
                            
                            
                            <button class="closebtn" @click="errorCloseModal">
                                閉じる
                                <i class="material-icons">close</i>
                            </button>
                        </selectModal>

                    </div>
                </div>
            
        </div>
        
        <div class="favorite-box">
            <table>
                <tbody>

                    <tr>
                        <th width="20" height="20"></th> <th>月</th> <th>火</th> <th>水</th> <th>木</th> <th>金</th> <th>土</th>
                    </tr>
                    <tr v-for ="(gen, g) of 7" :key="g">
                        <th width="20" height="70">{{gen}}</th>
                        <td v-for="(niti, n) in days" :key="n">
                            <p>{{ fillGen(gen, niti) }}</p>
                        </td>
                    </tr>

                </tbody>
            </table>
        </div>

        <div class="favorite-top">
            <h3>気になるリスト</h3>
        </div>

        <!-- 検索結果を表示 -->
        <div class="table-box" v-for="(value, index) in setFavorite" :key="index" >
            <div class="container">
                <div class="row">
                    <div class="col-sm-12 col-md-2">{{index+1}}.  {{value.kamoku}} </div>
                    <div class="col-sm-12 col-md-2 gakubu">{{value.gakubu}} <br class="pc">{{value.gakka}}</div>
                    <div class="col-sm-4 col-md-2"> {{value.tantou}}</div>
                    <div class="col-sm-4 col-md-1">{{value.kyoushitsu}}</div>
                    <div class="col-sm-4 col-md-2">{{value.gakki}}　{{value.niti}}{{value.gen}}　{{value.sou}}{{value.ji}}</div>
                    <div class="col-sm-12 col-md-2 d-flex align-items-center">{{value.bikou}}</div>
                    <div class="col-sm-12 col-md-1 d-flex align-items-center">
                        <input type="checkbox" :id="'value.kamoku' + index" :value="value" v-model="setFavorite">
                        <label :for="'value.kamoku' + index"> <i class="f_icon"></i> </label>
                        
                        <!--<input type="radio" id="s_one" :value="value" v-model="setFavorite">
                        <label for="s_one"><i class="material-icons">info_outline</i><br></label> -->
                        <!-- <i class="material-icons">info_outline</i> -->
                    </div>
                    
                </div>
            </div>
        </div>

        <!-- 0件のとき バナー表示 -->
        <div class="favorite-banner" v-if="setFavorite.length == 0">
            <img class="pc" src="~/assets/img/banner_pc.png">
            <img class="sp" src="~/assets/img/banner_sm.png">
        </div>

    </div>
</template>

<script>
import firebase from '@/plugins/firebase'
import selectModal from '@/components/selectModal.vue'
import passList from '@/assets/pass.json'

export default {
    components: {
        selectModal
    },

    data() {
        return {
            // モーダル状態管理
            modalFlagSave: false,
            modalFlagLoad: false,
            modalFlagError: false,

            // パスフレーズ
            passList: passList,
            pass:"",

            days: ['月', '火', '水', '木', '金', '土'],
            gen: '',
            niti: ''
        }
    },

    computed: {
        setFavorite: {
            get: function() {
                return this.$store.state.table.favorite;
            },
            set: function(favo) {
                this.$store.commit('table/setFavorite', favo)
            }
        },

        fillGen: function() {
            return function(gen, niti) {
                const genfilter = this.setFavorite
                        .flatMap(
                            value => value.gen == gen && value.niti == niti
                            ? [value.kamoku, "\n", "(", value.tantou, ")", "\n"]
                            : []
                        )
                return genfilter.join('')
            }
        }
    },

    methods: {
        // 保存する際の操作
        saveHandler() {
            this.generatePass()
            this.saveOpenModal()
            this.setTable()
        },
        // 読み込む際の動作
        loadHandler() {
            this.loadCloseModal()
            this.getTable()
        },

        // モーダル状態管理
        saveOpenModal() { this.modalFlagSave = true },
        saveCloseModal() { this.modalFlagSave = false },

        loadOpenModal() { this.modalFlagLoad = true },
        loadCloseModal() { this.modalFlagLoad = false },

        errorOpenModal() { this.modalFlagError = true },
        errorCloseModal() { this.modalFlagError = false },

        // ランダムでパス生成　→　文字列化
        generatePass () {
            var list = this.passList.map((obj) => {
                return obj.word;
            });
            const randomPass = []
            
            for(var i=0; i<3; i++) {
                const rand = Math.floor(Math.random() * list.length);
                randomPass.push(list[rand])
            }
            randomPass.push('')

            this.pass = randomPass.join('。');
        },

        // DBにセットする
        setTable () {
            const time = new Date()
            const db = firebase.firestore()
            db.collection('timetables').doc(this.pass)
                .set({
                    timestamp: time,
                    timetable: this.setFavorite,
                })
        },

        //　DBから取得する 
        getTable () {
            // 空文字の場合に”　”を入れる
            if(!this.pass.length) {
                this.pass = " "
            }

            const db = firebase.firestore()
            db.collection("timetables").doc(this.pass)
                .get()
                .then((doc) => {
                    if (doc.exists) {
                        //const getResult = []
                        console.log("Document data:", doc.data().timetable);
                        this.$store.commit('table/setFavorite', doc.data().timetable)
                    } else {
                        // doc.data() will be undefined in this case
                        console.log("No such document!");
                        this.errorOpenModal()
                    }
                }).catch((error) => {
                    console.log("Error getting document:", error);
                });
        }
    },
}
</script>

<style>
.closebtn.done {
    color: #FFF;
    background: #FFA100;
    border-color: #FFA100;
}
.closebtn.done i { color: #FFF; }

.closebtn.done:hover { color: #FFA100; background: #FFF; border-color: #FFA100; }

.favorite {
    margin: 1% 0;
}
.favorite-top {
    margin: 3% 5%;
}

.favorite-box {
    margin: 0 4%;
    overflow-x: scroll;
}

.favorite-box table {
    display: block;
    white-space: pre-line;
    border-collapse: collapse;
    background-color: #F2F2F2;
    font-size: 0.8rem;
    margin: 0 auto;
}

.favorite-box tbody {
    width: 100%;
    table-layout: fixed;
    display:table;
}

th, td {
    border: solid 1px #333; /* 線の種類 太さ 色 */
}

th {
    background-color: #868686;
    color: #FFF;
}

/* 気になるボタン */
.f_icon::before {
    content: '\e87d'; 
    font-family: 'Material Icons';
    font-style: normal;
    font-size: 24px;
    color: #FFA100;
    cursor: pointer;
}

/* バナー */
.favorite-banner { margin: 5% 0; text-align: center; }

.favorite-banner img { width:90%; max-width: 900px; margin: 0 auto; }

</style>