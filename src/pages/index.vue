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

                        <div class="col-md-6 order-md-1">
                            <!-- 検索フォーム コンポーネント -->
                            <search />
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-tab container">
            <!-- タブ -->
            <ul>
                <li :class="{ clickBtn: tab === 1 }" @click="tab = 1">
                    <i class="material-icons">search</i>
                    検索結果
                </li>
                <li :class="{ clickBtn: tab === 2 }" @click="tab = 2">
                    <i class="material-icons">favorite</i>
                    気になるリスト
                </li>
                <li :class="{ clickBtn: tab === 3 }" @click="tab = 3">
                    <i class="material-icons">help_outline</i>
                    使い方
                </li>
            </ul>
            <div class="content">
                <div v-show="tab === 1" class="content-item">
                    <!-- 検索結果　 コンポーネント -->
                    <results />
                </div>
                <div v-show="tab === 2" class="content-item">
                    <favorite />
                </div>
                <div v-show="tab === 3" class="content-item">
                    <h2>使い方</h2>
                </div>
            </div>
        </div>


    </div>
</template>

<script>
import search from '@/components/search.vue'
import results from '@/components/results.vue'
import selectModal from '@/components/selectModal.vue'
import favorite from '../components/favorite.vue'

export default {
    components: {
        search,
        results,
        selectModal,
        favorite
    },

    data: () => {
        return {
            tab: 1,
        }
    },    
}
</script>


<style>

/*---------------------------------
  
  1.header  検索フォーム・メッセージ
    1.背景
    2.メッセージ
    3.検索フォーム

  2.main    タブ

  3.mb      スマホ・タブレットcss
    1.タブレット
    2.スマホ

---------------------------------*/


/* モーダルコンポーネント ボタン*/
.checkbox { padding-bottom: 20px; line-height: 3em; }

.checkbox label {
  display: inline-block;
  background-color: #FFF;
  margin: 1% 0;
  padding: 0 20px;
  border-radius: 100px;
  border: 2px solid;
  border-color: #2D2D2D;
  line-height: 2.2em;
}


.help_link__button {
    display: inline-block;
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

.help_link__button:hover { color: #FFA100; border-color: #FFA100; }


.help_link__button:active {
    color: #FFF;
    border-color: #FFF;
    background-color: #FFA100;
}


.help_link__button i {
  position: absolute;
  top: 3px;
  right:20px;
  color: #2D2D2D;
}

.help_link__button:hover i{ color: #FFA100; }

.help_link__button:active i{ color: #FFF; }

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

.closebtn:hover { color: #FFA100; border-color: #FFA100; }

.closebtn:active {
    color: #FFF;
    border-color: #FFF;
    background-color: #FFA100;
}

.closebtn:hover i{ color: #FFA100; }

.closebtn:active i{ color: #FFF; }

/*---------------------------------
  
  1.header  検索フォーム・メッセージ

---------------------------------*/

.jumbotron {
    background:url(~/assets/img/background-img.png)
    center no-repeat; 
    background-size: cover;
}

/* トップメッセージ */
.top-message { margin: auto 0; padding: 50px 0 ; }

.top-message h1 { font-weight: 700; }

.top-message p {
    margin-top: 20px;
    font-size: 15px;
    color: #868686;
}


/*---------------------------------
  
  2.main  タブ

---------------------------------*/
ul {
    list-style: none;
    display: block;
    text-align: center;
    /* overflow: hidden; */
    overflow-x: auto;
    white-space: nowrap;
    margin: 1% 0;
    padding: 0;
    border-bottom: 1px solid #DDDDDD;
}
li {
    display: inline-block;
    color: #2D2D2D;
    height: 45px;
    border: 1px solid white;
    padding: 1px 20px;
}

li i {
    vertical-align: -6px;
    padding-right: 2px;
}

.clickBtn {
    border-bottom: 3px solid #FFA100;
    color: #FFA100;
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
.top-message { padding: 50px 4%; }

}


/* スマホ用 */
@media only screen and (max-width: 575px) {

/* トップメッセージ */
.top-message { padding: 50px 4%; }

}

</style>