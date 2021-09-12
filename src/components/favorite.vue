<template>
    <div class="favorite">
        <div class="favorite-top">
            <h3>"仮"時間割表</h3>
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
export default {
    data() {
        return {
            days: ['月', '火', '水', '木', '金', '土'],
            gen: '',
            niti: ''
        }
    },
    computed: {
        favorite: {
            get: function() {
                return this.$store.getters['table/timeTable'];
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

        fillGen: function() {
            return function(gen, niti) {
                const genfilter = this.setFavorite
                        .flatMap(
                            value => value.gen == gen && value.niti == niti
                            ? [value.kamoku, "(", value.tantou, ")", "\n"]
                            : []
                        )
                return genfilter.join('')
            }
        }

 
    }
}
</script>

<style>
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