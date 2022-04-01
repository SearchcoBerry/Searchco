<template>
    <div>
        <div class="header">
            <div class="jumbotron">
                <div class="container">
                    <div class="row">
                        <div class="top-message">
                            <p>シラバス参照</p>
                            <h1>{{searchSyllabus.subject}}</h1>
                            <p>
                                {{setSyllabus}}
                                {{searchSyllabus}}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
import com from '@/assets/syllabus/com_2021.json'
import econo from '@/assets/syllabus/econo_2021.json'
import gaikokujinn from '@/assets/syllabus/gaikokujinn_2021.json'
import global from '@/assets/syllabus/global_2021.json'
import industrial from '@/assets/syllabus/industrial_2021.json'
import low from '@/assets/syllabus/low_2021.json'
import qualification from '@/assets/syllabus/qualification_2021.json'

export default {
    data() {
        return {
            com: com,
            econo: econo,
            gaikokujinn: gaikokujinn,
            global: global,
            industrial: industrial,
            low: low,
            qualification: qualification
        }
    },

    computed: {
        setSyllabus: {
           get: function() {
               return this.$store.state.syllabus.syllabusData;
           },
           set: function(sValue) {
               this.$store.commit('syllabus/setSyllabus', sValue);
           }
        },

        searchSyllabus() {
            const syllabusData = [];

            switch (this.setSyllabus.gakubu) {
                case '共通科目':
                    console.log('共通科目');
                    syllabusData = com;
                    break;
                
                case '経済学部':
                    console.log('経済学部');
                    syllabusData = econo;
                    break;

                case '外国人留学生対象日本語科目':
                    console.log('外国人留学生対象日本語科目');
                    syllabusData = gaikokujinn;
                    break;

                case '総合文化学部':
                    console.log('総合文化学部');
                    syllabusData = global;
                    break;
                
                case '産業情報学部':
                    console.log('産業情報学部');
                    syllabusData = industrial;
                    break;

                case '法学部':
                    console.log('経済学部');
                    syllabusData = low;
                    break;

                case '資格科目':
                    console.log('資格科目');
                    syllabusData = qualification;
                    break;
            }

            return syllabusData.filter(value => {

                return value.subject.includes(this.setSyllabus.kamoku) ||
                        value.folder.includes(this.setSyllabus.gakka) || //gakka
                        value.semester.includes(this.setSyllabus.gakki) || //gakki
                        value.instructor.includes(this.setSyllabus.tantou)   //tantou
            
            })
        }
    }
}
</script>

