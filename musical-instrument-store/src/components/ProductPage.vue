<template>
    <h2>Страница продукта {{ prodId }}</h2>
    <div class="info-wrapper">
        <div class="info-wrapper__about about">
            <div class="about__photo photo">
                <div class="photo__img-wrapper">
                    <img :src="require('../assets/' + prodPhoto)"  :alt="`${prodPhoto}`" class="main-img">
                </div>
                <div class="photo__scroll-wrapper">
                    <carousel :items-to-show="4">
                        <slide v-for="item in photoList" :key="item">
                            <button @click="changePhoto(item)">
                                <img :src="require('../assets/' + item)" :alt="`${prodPhoto}`">
                            </button>
                        </slide>
                        <template #addons>
                        <navigation />
                        <pagination />
                        </template>
                    </carousel>
                </div>
            </div>
            <div class="about__cta-info">
                <div class="cta-wrapper">
                    <p class="price">2222 руб.</p>
                    <div class="buttons">
                        <button class="cta-btn">В избранное</button>
                        <button class="cta-btn">В корзину</button>
                    </div>
                </div>
                <div class="prod-info" >
                    <button @click="char" id="char" class="toggle-btn active">Описание</button>
                    <button @click="desc" id="desc" class="toggle-btn">Характеристики</button>
                    <p class="info-desc" v-if="show == 0">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dignissim id tortor ac mattis. Suspendisse lacinia vulputate nibh eu pharetra. Vestibulum consectetur auctor tellus, nec placerat ipsum tincidunt in. Nulla tempus sollicitudin ligula et congue. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi gravida, augue eu eleifend facilisis, est sapien lobortis urna, in aliquam velit ligula vel dolor. Duis ornare vulputate mauris sed tincidunt. Aliquam erat volutpat.
                    </p>
                    <p class="info-char" v-if="show == 1">ghdxfghdfgdfgdfg</p>
                </div>
            </div>
        </div>
        <div class="similar">
            <p class="similar__title">Похожие товары</p>
            <ul>
                <li v-for="item in CardsYouEnjoy" :key="item.id" class="similar__item">
                    <img :src="require('../assets/' + item.img)" :alt="`${item.img}`" class="similar_img">
                    <p>{{ item.name }}</p>
                    <p>{{ item.price }}</p>
                </li>
            </ul>
        </div>
        <CommentSection />
    </div>
</template>

<script>

import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';
import CommentSection from '@/components/CommentSection.vue';

export default {
    data() {
        return {
            photoList: ['prod1-1.jpg', 'prod1-2.jpg', 'prod1-3.jpg', 'prod1-4.jpg'],
            prodPhoto: 'prod1-0.jpg',
            show: 0,
            CardsYouEnjoy: [
                { id: 1, name: "Барабаны", img: "baraban-black.png", price: "13999 р" },
                { id: 2, name: "Гитара", img: "gitara.png", price: "12999 р" },
                { id: 3, name: "Баян", img: "bayan.png", price: "2999 р" },
                { id: 4, name: "Синтезатор", img: "cintezator.png", price: "10999 р" },
                // { id: 5, name: "Барабаны", img: "baraban-green.png", price: "13999 р" },
            ],
        }
    },
    components: {
        Carousel,
        Slide,
        Pagination,
        Navigation,
        CommentSection,
    },
    methods: {
        char() {
            if (this.show == 1) {
                document.getElementById('char').classList.toggle('active');
                document.getElementById('desc').classList.toggle('active');
            }
            this.show = 0;
        },
        desc() {
            if (this.show == 0) {
                document.getElementById('char').classList.toggle('active');
                document.getElementById('desc').classList.toggle('active');
            }
            this.show = 1;
        },
        changePhoto(name) {
            this.prodPhoto = name;
        },
    },
    computed: {
        prodId () {
            return this.$route.params.id;
        },
    }
}
</script>

<style>
h2 {
    margin: 50px auto;
    text-align: center;
}

.info-wrapper {
    margin: auto;
    max-width: 375px;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    padding: 0 15px;
    gap:  20px;
}

.photo__img-wrapper {
    max-width: 372px;
    min-height: 415px;
    border: 1px solid #000000;
    margin-bottom: 10px;
}

.main-img {
    min-height: 415px;
    margin: 0 auto;
}

.photos-item img {
    height: 100%;
}

.cta-wrapper {
    margin-bottom: 30px;
}

.price {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 30px;
}

.buttons {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    max-width: 385px;
}

.cta-btn {
    background: #FCBA06;
    border-radius: 15px;
    max-width: 185px;
    width: 100%;
    padding: 10px 15px;
}

.toggle-btn + .toggle-btn {
    margin-left: 20px;
}

.about__cta-info {
    max-width: 372px;
}

.toggle-btn {
    font-style: normal;
    font-weight: 700;
    font-size: 20px;
    line-height: 24px;
}

.active {
    text-decoration: underline;
}

.similar {
    max-width: 372px;
}

.similar ul {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
}

.similar__title {
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 39px;
    margin-bottom: 20px;
}

.similar__item {
    max-width: 150px;
    width: 100%;
    border: 1px solid black;
    border-radius: 15px;
    padding: 10px;
    min-height: 200px;
    margin-bottom: 25px;
}

.similar__item img {
    border-radius: 15px 15px 0 0;
    margin-bottom: 10px;
}

.about__photo {
        max-width: 372px;
        width: 100%;
    }

@media (min-width: 1000px) {
    .info-wrapper {
        max-width: 950px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .about__cta-info {
        display: flex;
        flex-direction: column;
        gap: 30px;
        max-width: 500px;
        width: 100%;
    }

    .similar {
        max-width: 900px;
    }

    .info-wrapper__about {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
}
</style>