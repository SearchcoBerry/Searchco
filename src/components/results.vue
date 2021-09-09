<template>
  <div class="main">
    <div class="row">
      <div class="col-sm-6 result">
        <div v-if="searchWords == ''">
          <h3>すべての検索結果</h3>
        </div>

        <div v-else>
          <h3>{{ searchWords }}の検索結果</h3>
        </div>

        <div v-if="searchKamoku.length >= 100">
          <p>{{ searchKamoku.length }}件 上位100件まで表示</p>
        </div>

        <div v-else>
          <p>{{ searchKamoku.length }}件</p>
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
              <div
                class="p-2 bd-highlight"
                v-for="(sort, s) in optionsSort"
                :key="s"
              >
                <input
                  :id="'sort' + s"
                  type="radio"
                  :value="sort"
                  v-model="selectedSort"
                />
                <label :for="'sort' + s"
                  ><span>{{ sort.label }}</span></label
                >
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
    <div
      class="table-box"
      v-for="(value, index) in sorted.slice(0, 100)"
      :key="index"
    >
      <div class="container">
        <div class="row">
          <div class="col-sm-12 col-md-2">
            {{ index + 1 }}. {{ value.kamoku }}
          </div>
          <div class="col-sm-12 col-md-2 gakubu">
            {{ value.gakubu }} <br class="pc" />{{ value.gakka }}
          </div>
          <div class="col-sm-4 col-md-2">{{ value.tantou }}</div>
          <div class="col-sm-4 col-md-2">{{ value.kyoushitsu }}</div>
          <div class="col-sm-4 col-md-2">
            {{ value.gakki }} <br />{{ value.niti }}曜 {{ value.gen }}限
          </div>
          <div class="col-sm-12 col-md-1 d-flex align-items-center">
            {{ value.bikou }}
          </div>
          <div class="col-sm-12 col-md-1 d-flex align-items-center">
            <input
              type="checkbox"
              :id="'value' + index"
              :value="value"
              v-model="setFavorite"
            />
            <label :for="'value' + index"> <i class="icon"></i> </label>

            <!--<input type="radio" id="s_one" :value="value" v-model="setFavorite" @click = "returnPDF(this.value.gakka, this.value.tantou, this,value.niti, this,value.gen)">
                            <label for="s_one"><i class="material-icons">info_outline</i><br></label> -->
            <i
              class="material-icons"
              @click="
                returnPDF(
                  value.kamoku,
                  value.gakka,
                  value.tantou,
                  value.niti,
                  value.gen
                )
              "
              >info_outline</i
            >
          </div>
        </div>
      </div>
    </div>

    <!-- 300件以上 エラー -->
    <div class="error-too-long" v-if="searchKamoku.length >= 300">
      <img src="~/assets/img/error.png" />
      <h2>
        あい!データが100件以上あるわけよ。<br />
        こんな沢山あったらあわてぃはーてぃーするから 条件絞ろうね〜
      </h2>
    </div>

    <!-- 0件　エラー -->
    <div class="error-too-long" v-if="searchKamoku.length == 0">
      <img src="~/assets/img/error.png" />
      <h2>おっと...「{{ searchWords }}」は見つからなかったみたいだ...</h2>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import selectModal from "@/components/selectModal.vue";
import lists from "@/assets/list-2.json";
//import pdf from "vue-pdf";

export default {
  components: {
    selectModal
    //pdf
  },

  data() {
    return {
      modalFlag: false,

      optionsSort: [
        { label: "科目名順", code: "kamoku" },
        { label: "教員名順", code: "tantou" },
        { label: "曜日順", code: "niti" },
        { label: "時限順", code: "gen" }
      ],
      gakka_to_filename: [
        {
          label: "人間文化科目群",
          code: "com_humanculture2021.pdf"
        },
        {
          label: "社会生活科目群",
          code: "com_sociallife2021.pdf"
        },
        {
          label: "自然環境科目群",
          code: "com_naturalenvironment2021.pdf"
        },
        {
          label: "国際理解科目群",
          code: "com_internationalunderstanding2021.pdf"
        },
        {
          label: "情報科目群",
          code: "com_information2021.pdf"
        },
        {
          label: "沖縄科目群",
          code: "com_okinawa2021.pdf"
        },
        {
          label: "健康科目群",
          code: "com_health2021.pdf"
        },
        {
          label: "外国語科目群（英語）",
          code: "com_english2021.pdf"
        },
        {
          label: "外国語科目群（英語以外）",
          code: "com_foreignlanguage2021.pdf"
        },
        {
          label: "キャリア科目群",
          code: "com_careereducation2021.pdf"
        },
        {
          label: "法律学科",
          code: "law_law2021.pdf"
        },
        {
          label: "地域行政学科",
          code: "law_regionaladministration2021.pdf"
        },
        {
          label: "経済学科",
          code: "econo_economics2021.pdf"
        },
        {
          label: "地域環境政策学科",
          code: "econo_regionalenvironmentalpolicy2021.pdf"
        },
        {
          label: "企業システム学科",
          code: "industrial_businessadministration2021.pdf"
        },
        {
          label: "産業情報学科",
          code: "industrial_industrialinformation2021.pdf"
        },
        {
          label: "日本文化学科",
          code: "global_japaneselanguageandculture2021.pdf"
        },
        {
          label: "英米言語文化学科",
          code: "global_britishandamericanlanguage2021.pdf"
        },
        {
          label: "社会文化学科",
          code: "global_societyandregionalculture2021.pdf"
        },
        {
          label: "人間福祉学科",
          code: "global_humanwelfare2021.pdf"
        },
        {
          label: "南島文化専攻",
          code: "gr_rc_ryukyuanculture2021.pdf"
        },
        {
          label: "英米言語文化専攻",
          code: "gr_rc_britishandamericanstudies2021.pdf"
        },
        {
          label: "人間福祉専攻",
          code: "gr_rc_humanwelfare2021.pdf"
        },
        {
          label: "地域産業専攻",
          code: "gr_regionalbusinessandeconomics2021.pdf"
        },
        {
          label: "法律学専攻",
          code: "gr_law2021.pdf"
        },
        {
          label: "教職課程",
          code: "qualification_tp2021.pdf"
        },
        {
          label: "博物館学芸員",
          code: "qualification_museum2021.pdf"
        },
        {
          label: "図書館司書",
          code: "qualification_library2021.pdf"
        },
        {
          label: "学校図書館司書教諭",
          code: "qualification_schoollibrary2021.pdf"
        },
        {
          label: "上級情報処理士／上級ビジネス実務士",
          code: "qualification_informationprocessing2021.pdf"
        },
        {
          label: "社会福祉士",
          code: "qualification_socialworker2021.pdf"
        },
        {
          label: "精神保健福祉士",
          code: "qualification_psychiatricsocialworker2021.pdf"
        },
        {
          label: "スクール・ソーシャルワーカー",
          code: "qualification_ssocialworker2021.pdf"
        },
        {
          label: "日本語教員",
          code: "qualification_japaneseteacher2021.pdf"
        },
        {
          label: "公認心理師",
          code: "qualification_licensed psychologists2021.pdf"
        },
        {
          label: "日本語科目",
          code: "gaikokujinn_nihongo2021.pdf"
        },
        {
          label: "実務経験のある教員等による授業科目",
          code: "jitsumu_jitsumu2021.pdf"
        }
      ],

      lists: lists,

      formResult: "",
      seasonResult: "",
      hourResult: "",
      daysResult: ""
    };
  },

  methods: {
    openModal() {
      this.modalFlag = true;
    },
    closeModal() {
      this.modalFlag = false;
    },
    returnPDF(kamoku, gakka, tantou, niti, gen) {
      console.log(kamoku, gakka, tantou, niti, gen);
      let return_url = this.gakka_to_filename.findIndex(
        ({ label }) => label === gakka
      );
      console.log(return_url);
      var tantou = tantou.replace(/\s+/g, "");
      var url = this.gakka_to_filename[return_url].code;
      var url = url.slice(0, -4);
      let json = require(`~/assets/Syllabus/` + url + `.json`);
      let niti_gen = niti + gen;

      let return_json = json.findIndex(
        json =>
          json.subject_name === kamoku &&
          json.subject_teacher === tantou &&
          json.subject_schedule == niti_gen
      );
      console.log("return_json:" + return_json);
      console.log(json[return_json]);
    }
  },

  computed: {
    ...mapState([
      "searchWords",
      "selectedSeason",
      "selectedForm",
      "selectedDays",
      "selectedTimes",
      "selectedSort"
    ]),

    selectedSort: {
      get: function() {
        return this.$store.state.selectedSort;
      },
      set: function(sort) {
        this.$store.commit("setSort", sort);
      }
    },

    setFavorite: {
      get: function() {
        return this.$store.state.table.favorite;
      },
      set: function(favo) {
        this.$store.commit("table/setFavorite", favo);
      }
    },

    replaceWords() {
      return this.searchWords.replace(/ /g, "　");
    },

    sorted() {
      switch (this.selectedSort.code) {
        default:
        case "kamoku": // 科目名順
          return this.searchKamoku.sort((a, b) => {
            return a.kamoku.localeCompare(b.kamoku, "ja");
          });
          break;

        case "tantou": // 教員名順
          return this.searchKamoku.sort((a, b) => {
            return a.tantou.localeCompare(b.tantou, "ja");
          });
          break;

        case "niti": // 曜日順
          const daysOrder = ["月", "火", "水", "木", "金", "土", "日"];
          return this.searchKamoku.sort((a, b) => {
            return daysOrder.indexOf(a.niti) - daysOrder.indexOf(b.niti);
          });
          break;

        case "gen": //　 時限順
          return this.searchKamoku.sort((a, b) => {
            return a.gen.localeCompare(b.gen, "ja");
          });
          break;
      }
    },

    searchKamoku() {
      return this.lists.filter(value => {
        //--- 授業形態　フィルター ---//
        const form = this.selectedForm;

        if (form == "online") {
          this.formResult = value.kyoushitsu.match("^(?=.*ｵﾝﾗｲﾝ授業).*$");
        } else if (form == "real") {
          this.formResult = value.kyoushitsu.match("^(?!.*ｵﾝﾗｲﾝ授業).*$");
        } else {
          this.formResult = value.kyoushitsu.match("(?=.)");
        }

        //--- 学期 フィルター ---//
        const season = this.selectedSeason;

        if (season == "season0") {
          this.seasonResult = value.gakki.match("^(?=.*通年).*$");
        } else if (season == "season1") {
          this.seasonResult = value.gakki.match("^(?=.*前期).*$");
        } else if (season == "season2") {
          this.seasonResult = value.gakki.match("^(?=.*後期).*$");
        } else {
          this.seasonResult = value.gakki.match("(?=.)");
        }

        //--- 時限 フィルター ---//
        const times = this.selectedTimes;

        if (times && times.length) {
          this.hourResult = value.gen.match("[" + times.join("") + "]");
        } else {
          this.hourResult = value.gen.match("[1234567]");
        }

        //--- 曜日 フィルター ---//
        const days = this.selectedDays;

        if (days && days.length) {
          this.daysResult = value.niti.match(
            "[" + this.selectedDays.join("") + "]"
          );
        } else {
          this.daysResult = value.niti.match("[月火水木金土]");
        }

        return (
          this.formResult &&
          this.seasonResult &&
          this.hourResult &&
          this.daysResult &&
          (value.kamoku.includes(this.searchWords) ||
            value.gakubu.includes(this.searchWords) ||
            value.gakka.includes(this.searchWords) ||
            value.tantou.includes(this.replaceWords))
        );
      });
    }
  }
};
</script>

<style>
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

/* 検索結果テーブル */
.table-box {
  margin: 1% 4%;
  padding: 1%;
  border-radius: 15px;
  background-color: #f2f2f2;
}

/* 検索結果テーブル アイコン */
/* ラジオボタン */

/* ラジオボタン非表示は search.vue 250行付近 */

/* 順番並べ替え */
.sort label {
  display: inline-block;
  background-color: #fff;
  margin: 1% 0;
  padding: 0 20px;
  border-radius: 100px;
  border: 2px solid;
  border-color: #2d2d2d;
}

.sort input[type="radio"]:checked + label {
  background-color: #ffa100;
  color: #fff;
  border: 1px solid;
  border-color: #ffa100;
}

.sort input[type="checkbox"]:checked + label {
  background-color: #ffa100;
  color: #fff;
  border: 1px solid;
  border-color: #ffa100;
}

/* 気になるボタン */
.icon::before {
  content: "\e87e";
  font-family: "Material Icons";
  font-style: normal;
  font-size: 24px;
  color: #2d2d2d;
}

.table-box input[type="checkbox"]:checked ~ label .icon::before {
  content: "\e87d";
  font-family: "Material Icons";
  font-style: normal;
  font-size: 24px;
  color: #ffa100;
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

/* タブレット　*/

@media only screen and (max-width: 766px) {
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
