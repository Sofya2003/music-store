<template>
    <div class="wrapper">
        <h2>Блог</h2>
        <ul class="cards-list">
            <li v-for="item in newsList" :key="item.id" class="news-card">
                <img :src="require('../assets/' + item.img)" alt="img">
                <a href="">
                    <p class="title">{{ item.title }}</p>
                </a>
                <a href="">
                    <p class="desc">{{ item.desc }}</p>
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            newsList: [{title: 'title1', desc: 'desc1', img: 'news1.jpg'},
            {title: 'title2', desc: 'desc2', img: 'news2.jpg'},
            {title: 'title3', desc: 'desc3', img: 'news3.jpg'},
            {title: 'title4', desc: 'desc4', img: 'news4.jpg'}]
        }
    }
}
</script>

<style scoped>
h2 {
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 29px;
}

.cards-list {
    max-width: 380px;
    width: 100%;
    margin: 0 auto;
}
.news-card {
    margin: 0 auto 36px;
    max-width: 372px;
    min-height: 487px;
    border: 1px solid rgba(0, 0, 0, 0.39);
    box-shadow: 0px 0px 7px 3px rgba(0, 0, 0, 0.14);
    border-radius: 15px;
}

.news-card img {
    
    border-radius: 15px 15px 0 0;
}
.title {
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 29px;
    margin-top: 6px;
    margin-left: 23px;
}
.desc {
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 19px;
    margin-top: 6px;
    margin-left: 23px;
}

@media (min-width: 1000px) {
    .cards-list {
        max-width: 900px;
        width: 100%;
        display: flex;
        flex-wrap: wrap;
    }
}
</style>