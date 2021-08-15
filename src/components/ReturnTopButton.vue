<template>
    <div class="return-bt">
        <button @click="returnTop" >
            <i class="material-icons">arrow_upward</i>
        </button>
    </div>
</template>


<script>
export default {
    data() {
        return {
            buttonActive: false,
            scroll: 0
        }
    },

    mounted() {
        window.addEventListener('scroll', this.scrollWindow)
    },

    methods: {
        returnTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            })
        },

        scrollWindow() {
            const top = 100 // ボタンを表示させたい位置
            this.scroll = window.scrollY
            if (top <= this.scroll) {
                this.buttonActive = true
            } else {
                this.buttonActive = false
            }
        }
    }
}
</script>


<style>
.return-bt button {
    position: fixed;
    width: 60px;
    height: 60px;
    right: 40px;
    bottom: 40px;
    border-radius: 100px;
    border: none;
    box-shadow: 0 3px 5px rgba(0, 0, 0, .3);
}

i {
    padding-top: 5px;
}

.button-enter-active,
.button-leave-active {
  transition: opacity 0.5s;
}
.button-enter,
.button-leave-to {
  opacity: 0;
}
</style>