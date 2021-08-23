<template>
    <div class="favorite">
        <div class="favorite-top">
            <h3>"仮"時間割表</h3>
        </div>
        
        <div class="favorite-box row">
            <table>
                <tbody>

                    <tr>
                        <th></th>
                        <th>月</th>
                        <th>火</th>
                        <th>水</th>
                        <th>木</th>
                        <th>金</th>
                        <th>土</th>
                    </tr>
                    <tr v-for ="(gen, g) of 7" :key="g">
                        <th>{{gen}}</th>
                        <td v-for="(niti, n) in days" :key="n">
                            <p>{{ fillGen(gen, niti) }}</p>
                        </td>
                    </tr>

                </tbody>
            </table>


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

        fillGen: function() {
            return function(gen, niti) {
                const genfilter = this.favorite
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
    margin: 1% 5%;
}
.favorite-top {
    margin: 3% 0;
}

.favorite-box {
    margin: 1% 10%;
}

table {
    table-layout: fixed;
    width: 500px;
    white-space: pre-line;
    border-collapse: collapse;
    background-color: #F2F2F2;
}

th, td {
    height: 60px;
    border: solid 1px #333; /* 線の種類 太さ 色 */
}

th {
    background-color: #868686;
    color: #FFF;
}

</style>