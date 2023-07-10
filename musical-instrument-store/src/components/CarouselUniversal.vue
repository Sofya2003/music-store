<template>
  <div class="slider relative   h-[300px ] sm:h-[300px] md:h-[400px] lg:h-[500px]   w-full mt-[7px] mx-auto mb-6 lg:mb-20 sm:w-[600px] md:w-[700px] lg:w-[900px] lg:mt-[30px] xl:w-[1100px]">
    <div class="slider__track" :style="{ transform: `translateX(${-currentSlide * 100}%)` }">
      <div v-for="(slide, index) in photos" :key="index" class="slide">
        <img :src="require('../assets/'+ slide)" alt="Slide" class="slide__img">
      </div>
    </div>
    <div class="slider__controls">
      <button class="slider__prev" @click="prevSlide" :disabled="currentSlide === 0">&#10094;</button>
      <button class="slider__next" @click="nextSlide" :disabled="currentSlide === this.totalSlides - 1">&#10095;</button>
    </div>
  </div>
</template>
  
  <script>
    export default {
      props: {
        photos: {
          type: Array,
        }
      },

      data() {
        return {
          currentSlide: 0,
          totalSlides: 3
        }
      },
      methods: {
        prevSlide() {
          if (this.currentSlide > 0) this.currentSlide--;
        },
        nextSlide() {
          if (this.currentSlide < this.totalSlides - 1) this.currentSlide++;
        }
      }
    }
  </script>
  

  <style>
  .slider {
    overflow: hidden;
  }
  
  .slider__track {
    display: flex;
    transition: transform 0.5s ease;
    height: 100%;
  }
  
  .slide {
    flex: 0 0 100%;
    height: 100%;
  }
  
  .slide__img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .slider__controls {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0 20px;
    box-sizing: border-box;
    z-index: 1;
  }
  
  .slider__prev,
  .slider__next {
    font-size: 30px;
    background: transparent;
    border: none;
    color: white;
    cursor: pointer;
    outline: none;
    user-select: none;
  }
  
  .slider__prev:disabled,
  .slider__next:disabled {
    opacity: 0.5;
    cursor: default;
  }
  </style>