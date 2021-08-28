<template>
    <div class="header-nav">
        <div class="container">
            <div class="row">
                <div class="col logo">
                    <nuxt-link to="/">
                        <img src="~/assets/img/logo.png" alt="さちこ | トップ">
                    </nuxt-link>
                </div>
                
                <div class="col system-name pc">
                    <p>授業検索エンジン さちこ ver1.1 🥳</p>
                </div>
            </div>
            
            
        </div>
    </div>
</template>

<script>
	export default {
		components: {}
	};
</script>

<style>
.header-nav{
    height: 60px;
    background-color: #2D2D2D;
}

.logo img {
    height: 30px;
    width: auto;
    margin: 15px 8%;
}

.system-name {
    margin: auto 4%;
}

.system-name p {
    text-align: right;
    color: #FFF;
}


@media only screen and (max-width: 766px) {

.logo img {
    height: 35px;
    margin: 12px 3%;
}

}
</style>