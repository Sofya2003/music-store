<template>
    <div class="mr-4 ml-4 mb-4 w-[240px] p-4 border-2 border-gray-900 rounded-md  shadow-md flex flex-col justify-between"
            v-for="card in cards"
            :key="card.article"
            :title="card.name"
    >
    <router-link :to="{name: 'ProductPage', params: {id: card.article}}">
        <img 
                class="object-cover object-center w-full rounded-md  dark:bg-gray-500 h-52"
                :src="`${card.main_img}`"
        />

        <div class="mt-6 mb-2">
            <span class="block text-xs font-medium tracking-widest uppercase dark:text-violet-400">{{ card.name }}</span>
        </div>
        <p class="dark:text-gray-100">{{ card.price }}</p>
    </router-link>
    </div>
</template>



<script>
export default {
    name: "CardsItem",
    props: {
        cards: {
            type: Array
        },
  }
  }

</script>

