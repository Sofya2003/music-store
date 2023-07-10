
<template>
    <div>

        <CarouselUniversal v-bind:photos="state.photosCarousel"/>
        
        <p class="text-[24px] ml-6 sm:ml-20 mb-6 ">Возможно, вам понравится</p>
        
        <div class="mb-20 flex justify-start flex-wrap w-250 px-4 sm:px-[60px] md:px-[100px] lg:px-[90px] xl:px-[120px] 2xl:p-0 2xl:w-[1380px] mx-auto ">
            <div class="mr-4 ml-4 mb-4 w-[240px] p-4 border-2 border-gray-900 rounded-md  shadow-md flex flex-col justify-between"
                    v-for="card in state.CardsYouEnjoy"
                    :key="card.id"
                    :title="card.name"
            >
                <img :src="require('../assets/'+ card.img)" alt="" class="object-cover object-center w-full rounded-md  dark:bg-gray-500">

                <div class="mt-6 mb-2">
                    <span class="block text-xs font-medium tracking-widest uppercase dark:text-violet-400">{{ card.name }}</span>
                </div>
                <p class="dark:text-gray-100">{{ card.price }}</p>
            </div>
        </div>
        

        
    
    
        <p class="text-[24px] ml-6 sm:ml-20 mb-6 ">Вы ранее смотрели:</p>
        
        <div class="mb-20 flex justify-start flex-wrap w-250 px-4 sm:px-[60px] md:px-[100px] lg:px-[90px] xl:px-[120px] 2xl:p-0 2xl:w-[1380px] mx-auto ">
            <div class="mr-4 ml-4 mb-4 w-[240px] p-4 border-2 border-gray-900 rounded-md  shadow-md flex flex-col justify-between"
                    v-for="card in state.CardsYouEnjoy"
                    :key="card.id"
                    :title="card.name"
            >
                <img :src="require('../assets/'+ card.img)" alt="" class="object-cover object-center w-full rounded-md  dark:bg-gray-500">

                <div class="mt-6 mb-2">
                    <span class="block text-xs font-medium tracking-widest uppercase dark:text-violet-400">{{ card.name }}</span>
                </div>
                <p class="dark:text-gray-100">{{ card.price }}</p>
            </div>
        </div>



        
    
    
    </div>
</template>
    



<script>

import { reactive } from 'vue'


export default {
    name: "MainPage",
    setup() {
        const state = reactive({
            CardsYouEnjoy: [
                { id: 1, name: "Барабаны", img: "baraban-black.png", price: "13999 р" },
                { id: 2, name: "Гитара", img: "gitara.png", price: "12999 р" },
                { id: 3, name: "Баян", img: "bayan.png", price: "2999 р" },
                { id: 4, name: "Синтезатор", img: "cintezator.png", price: "10999 р" },
                { id: 5, name: "Барабаны", img: "baraban-green.png", price: "13999 р" },
            ],
            photosCarousel: ["slider1.png", "slider2.png", "slider1.png"]
        });
        
        return {
            state
        };
    }
}
</script>


