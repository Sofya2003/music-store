<template>
    <div v-if="visibleCatalogDesktop" class="w-full bg-white h-[600px] shadow-lg shadow-gray-500/40 mb-10 flex justify-center p-6">
      <div class="flex text-[18px] w-[710px] flex-wrap">

              <div v-on:click="setCategory(1)" class="mb-4 w-[220px] mr-4" >

                <img src="../assets/catalog-guitar.png" class="" alt="каталог гитары">
                <p v-on:click="setCategory(1)" class="ml-2">Гитары</p>

              </div>


              <div v-on:click="setCategory(2)" class="mb-4 w-[220px]  mr-4" >

                <img src="../assets/catalog-ukulele.png" class="" alt="каталог укулеле">
                <p v-on:click="setCategory(2)" class="ml-2">Укулеле</p>

              </div>


              <div v-on:click="setCategory(3)" class="mb-4 w-[220px]" >
                <img src="../assets/catalog-pianino.png" class="" alt="каталог клавишные">
                <p v-on:click="setCategory(3)" class="ml-2">Клавишные</p>
              </div>


              <div v-on:click="setCategory(4)" class="mb-4 w-[220px]  mr-4" >
                <img src="../assets/catalog-brass-instruments.png" class="" alt="каталог духовые">
                <p v-on:click="setCategory(4)" class="ml-2">Духовые</p>
              </div>


              <div v-on:click="setCategory(5)" class="mb-4 w-[220px]  mr-4" >
                <img src="../assets/catalog-drums.png" class="" alt="каталог ударные">
                <p v-on:click="setCategory(5)" class="ml-2">Ударные</p>
              </div>

              <div v-on:click="setCategory(6)" class="mb-4 w-[220px]" >
                <img src="../assets/catalog-accordion.png" class="" alt="каталог баяны и аккордионы">
                <p v-on:click="setCategory(6)" class="ml-2">Баяны, аккордионы</p>
              </div>

      </div>

    </div>
</template>

<script>


 export default {
  name: 'App',

  props: {
        visibleCatalogDesktop: {
          type: Boolean,
        }
      },

  data: () => ({
      selectCategory: '',
    }),

    methods: {
        setCategory(cat) {
          this.$emit('updateVisibleCatalog');
          this.selectCategory = cat;
          this.$router.push({ name: 'CatalogSection', params: { catalogcategory: this.selectCategory } })
          this.$store.dispatch('GET_INSTRUMENTS_FILTER_CATEGORY', cat);
          this.$store.dispatch('GET_SUBCATEGORY_FILTER_CATEGORY', cat);
        },
        
      }
 }
</script>