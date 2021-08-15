<template>
    <transition name="modal" appear>
        <div class="modal__overlay"  @click.self="closeModal">
            <div class="modal__window">
                <div class="modal__content">
                <slot />
                </div>
            </div>
        </div>
    </transition>
</template>

<script>
export default {
    methods: {
        closeModal() {
            this.$emit('close-modal')
        }
    }
}
</script>

<style>
.modal__overlay {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 100;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background: rgba(0, 0, 0, 0.7);
}

.modal__window {
    width: 50%;
    overflow: hidden;
    background-color: #FFF;
    border-radius: 20px;
}

.modal__content {
    height: 100%;
    padding: 30px;
}

/* タブレット　*/ 

@media only screen and (max-width: 538px) {
    .modal__window {
        
        width: 80%;
    }
}


/* transition */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.2s;
}

.modal-enter-active,
.modal-leave-active
.modal__window {
    transition: opacity 0.2s, transform 0.2s;
  }

.modal-leave-active {
  transition: opacity 0.4s ease 0.2s;
}

.modal-enter,
.modal-leave-to {
  opacity: 0;
}

.modal-enter,
.modal-leave-to 
.modal__window {
    opacity: 0;
    transform: translateY(-20px);
  } 
</style>
