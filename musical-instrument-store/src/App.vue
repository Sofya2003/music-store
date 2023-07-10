<template>
  <div>
  <div class="flex flex-col h-screen justify-between">


  <!-- ВЕРСИЯ ХЕДЕРА DESKTOP -->
      <header class="h-[180px] bg-gradient-to-b from-[#220000] to-[#580005] to-43.47% p-10 hidden xl:block">
      <nav class="h-full">
        <div class="flex flex-row">
          <div class="w-[180px] mr-32">
            <router-link to="/" class="block ">
              <img src="./assets/logo.png" alt="Логотип" class=" block h-[110px] w-[110px]">
            </router-link>
          </div>

          <div class="w-full text-white text-[20px] flex flex-col justify-between mr-12">
            <div class="flex justify-end">
              <router-link to="/" class="mr-6">
                <p>
                  Главная
                </p>
              </router-link>

              <p class="mr-6">
                О нас
              </p>

              <p class="mr-6">
                Доставка и оплата
              </p>

              <router-link to="/blog" class="mr-6">
                <p>
                  Блог
                </p>
              </router-link>

              <p>
                Контакты
              </p>
            </div>
            

            <div  class="flex justify-end">

              <button v-on:click="visibleCatalogDesktop=!visibleCatalogDesktop" type="button" class="mr-6 text-black py-0 px-6 block flex justify-items items-center  rounded-md border border-transparent bg-white">
                <span class="mr-8 text-[18px]">
                  Каталог
                </span>
                
                <svg viewBox="0 0 40 25" width="35" height="35">
                  <rect width="40" height="5"></rect>
                  <rect y="10" width="40" height="5"></rect>
                  <rect y="20" width="40" height="5"></rect>
                </svg>
              </button>

             
             
              <div class="relative max-w-xs mr-32">
                    <label for="hs-table-search" class="sr-only">Поиск</label>
                    <input type="text" name="hs-table-search" id="hs-table-search" class="text-[18px] p-2 pl-16 block w-full border-black rounded-md  focus:border-blue-500 focus:ring-blue-500 text-black" placeholder="Поиск">
                    <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none pl-4">
                      <svg class="h-3.5 w-3.5 text-black" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="black" viewBox="0 0 16 16">
                        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                      </svg>
                    </div>
              </div>


              <a href="#" class="mr-8">
                <svg width="40" height="36" viewBox="0 0 40 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M11 0.60889C4.925 0.60889 0 5.63197 0 11.828C0 23.047 13 33.2462 20 35.6185C27 33.2462 40 23.047 40 11.828C40 5.63197 35.075 0.60889 29 0.60889C25.28 0.60889 21.99 2.49267 20 5.37597C18.9857 3.90241 17.6382 2.69981 16.0715 1.87C14.5049 1.0402 12.7653 0.607617 11 0.60889Z" fill="white"/>
                </svg>
              </a>

              <a href="#" class="mr-16">
                <svg width="46" height="38" viewBox="0 0 46 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M43.125 17.5564C43.9186 17.5564 44.5962 17.8339 45.1577 18.3888C45.7192 18.9437 46 19.6133 46 20.3976C46 21.1819 45.7192 21.8515 45.1577 22.4064C44.5962 22.9614 43.9186 23.2388 43.125 23.2388H42.7881L40.2051 37.9331C40.0853 38.6138 39.7559 39.1761 39.2168 39.6201C38.6777 40.064 38.0638 40.286 37.375 40.286H8.625C7.9362 40.286 7.32227 40.064 6.7832 39.6201C6.24414 39.1761 5.91471 38.6138 5.79492 37.9331L3.21191 23.2388H2.875C2.08138 23.2388 1.40381 22.9614 0.842285 22.4064C0.280762 21.8515 0 21.1819 0 20.3976C0 19.6133 0.280762 18.9437 0.842285 18.3888C1.40381 17.8339 2.08138 17.5564 2.875 17.5564H43.125ZM10.8936 35.3139C11.2829 35.2843 11.6086 35.1178 11.8706 34.8145C12.1326 34.5111 12.2487 34.1671 12.2188 33.7823L11.5 24.5484C11.4701 24.1637 11.3016 23.8418 10.9946 23.5829C10.6877 23.3239 10.3395 23.2092 9.9502 23.2388C9.56087 23.2684 9.23519 23.4349 8.97314 23.7382C8.7111 24.0416 8.59505 24.3857 8.625 24.7704L9.34375 34.0043C9.3737 34.3742 9.52718 34.685 9.8042 34.9365C10.0812 35.1881 10.4069 35.3139 10.7812 35.3139H10.8936ZM20.125 33.8933V24.6594C20.125 24.2747 19.9827 23.9417 19.6982 23.6606C19.4137 23.3794 19.0768 23.2388 18.6875 23.2388C18.2982 23.2388 17.9613 23.3794 17.6768 23.6606C17.3923 23.9417 17.25 24.2747 17.25 24.6594V33.8933C17.25 34.278 17.3923 34.611 17.6768 34.8922C17.9613 35.1733 18.2982 35.3139 18.6875 35.3139C19.0768 35.3139 19.4137 35.1733 19.6982 34.8922C19.9827 34.611 20.125 34.278 20.125 33.8933ZM28.75 33.8933V24.6594C28.75 24.2747 28.6077 23.9417 28.3232 23.6606C28.0387 23.3794 27.7018 23.2388 27.3125 23.2388C26.9232 23.2388 26.5863 23.3794 26.3018 23.6606C26.0173 23.9417 25.875 24.2747 25.875 24.6594V33.8933C25.875 34.278 26.0173 34.611 26.3018 34.8922C26.5863 35.1733 26.9232 35.3139 27.3125 35.3139C27.7018 35.3139 28.0387 35.1733 28.3232 34.8922C28.6077 34.611 28.75 34.278 28.75 33.8933ZM36.6562 34.0043L37.375 24.7704C37.4049 24.3857 37.2889 24.0416 37.0269 23.7382C36.7648 23.4349 36.4391 23.2684 36.0498 23.2388C35.6605 23.2092 35.3123 23.3239 35.0054 23.5829C34.6984 23.8418 34.5299 24.1637 34.5 24.5484L33.7812 33.7823C33.7513 34.1671 33.8674 34.5111 34.1294 34.8145C34.3914 35.1178 34.7171 35.2843 35.1064 35.3139H35.2188C35.5931 35.3139 35.9188 35.1881 36.1958 34.9365C36.4728 34.685 36.6263 34.3742 36.6562 34.0043ZM10.6914 6.99075L8.60254 16.1358H5.6377L7.90625 6.34704C8.19075 5.04483 8.8571 3.98308 9.90527 3.1618C10.9535 2.34052 12.1514 1.92987 13.499 1.92987H17.25C17.25 1.54513 17.3923 1.21218 17.6768 0.931017C17.9613 0.649857 18.2982 0.509277 18.6875 0.509277H27.3125C27.7018 0.509277 28.0387 0.649857 28.3232 0.931017C28.6077 1.21218 28.75 1.54513 28.75 1.92987H32.501C33.8486 1.92987 35.0466 2.34052 36.0947 3.1618C37.1429 3.98308 37.8092 5.04483 38.0938 6.34704L40.3623 16.1358H37.3975L35.3086 6.99075C35.1439 6.33964 34.8032 5.80692 34.2866 5.39258C33.77 4.97824 33.1748 4.77107 32.501 4.77107H28.75C28.75 5.15581 28.6077 5.48876 28.3232 5.76992C28.0387 6.05108 27.7018 6.19166 27.3125 6.19166H18.6875C18.2982 6.19166 17.9613 6.05108 17.6768 5.76992C17.3923 5.48876 17.25 5.15581 17.25 4.77107H13.499C12.8252 4.77107 12.23 4.97824 11.7134 5.39258C11.1968 5.80692 10.8561 6.33964 10.6914 6.99075Z" fill="white"/>
                </svg>
              </a>

              <router-link to="/login" class="mr-6">
                <p class="mr-8">
                  Вход
                </p>
              </router-link>

              <router-link to="/register" class="mr-6">
                <p >
                  Регистрация
                </p>
              </router-link>


            </div>
          </div>
        </div>
      </nav>
    </header>


    <!-- РАЗВЕРНУТЫЙ КАТАЛОГ DESKTOP HEADER -->


    <CatalogDropdownDesktop
      v-bind:visibleCatalogDesktop="visibleCatalogDesktop"
      @updateVisibleCatalog="updateVisibleCatalog"
    />
    



<!-- МОБИЛЬНАЯ ВЕРСИЯ HEADER -->

    <header class="h-[60px] bg-gradient-to-b from-[#220000] to-[#580005] to-43.47% p-4 xl:hidden">
      <nav class="h-full">
            <div  class="flex justify-between ">


              <!-- три полоски -->

              <button v-on:click="visibleMenu=!visibleMenu">
                <svg viewBox="0 0 40 25" width="24" height="22" fill="white">
                    <rect width="40" height="5"></rect>
                    <rect y="10" width="40" height="5"></rect>
                    <rect y="20" width="40" height="5"></rect>
                </svg>
              </button>


              <div class="flex justify-end">
                <!-- поиск -->
                <svg class="h-[22px] w-[22px] text-black mr-3" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="white" viewBox="0 0 16 16">
                  <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                </svg>

                <!-- избранное -->
                <a href="#" class="mr-3">
                  <svg width="24" height="22" viewBox="0 0 40 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11 0.60889C4.925 0.60889 0 5.63197 0 11.828C0 23.047 13 33.2462 20 35.6185C27 33.2462 40 23.047 40 11.828C40 5.63197 35.075 0.60889 29 0.60889C25.28 0.60889 21.99 2.49267 20 5.37597C18.9857 3.90241 17.6382 2.69981 16.0715 1.87C14.5049 1.0402 12.7653 0.607617 11 0.60889Z" fill="white"/>
                  </svg>
                </a>

                <!-- корзина -->
                <a href="#">
                  <svg width="24" height="22" viewBox="0 0 46 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M43.125 17.5564C43.9186 17.5564 44.5962 17.8339 45.1577 18.3888C45.7192 18.9437 46 19.6133 46 20.3976C46 21.1819 45.7192 21.8515 45.1577 22.4064C44.5962 22.9614 43.9186 23.2388 43.125 23.2388H42.7881L40.2051 37.9331C40.0853 38.6138 39.7559 39.1761 39.2168 39.6201C38.6777 40.064 38.0638 40.286 37.375 40.286H8.625C7.9362 40.286 7.32227 40.064 6.7832 39.6201C6.24414 39.1761 5.91471 38.6138 5.79492 37.9331L3.21191 23.2388H2.875C2.08138 23.2388 1.40381 22.9614 0.842285 22.4064C0.280762 21.8515 0 21.1819 0 20.3976C0 19.6133 0.280762 18.9437 0.842285 18.3888C1.40381 17.8339 2.08138 17.5564 2.875 17.5564H43.125ZM10.8936 35.3139C11.2829 35.2843 11.6086 35.1178 11.8706 34.8145C12.1326 34.5111 12.2487 34.1671 12.2188 33.7823L11.5 24.5484C11.4701 24.1637 11.3016 23.8418 10.9946 23.5829C10.6877 23.3239 10.3395 23.2092 9.9502 23.2388C9.56087 23.2684 9.23519 23.4349 8.97314 23.7382C8.7111 24.0416 8.59505 24.3857 8.625 24.7704L9.34375 34.0043C9.3737 34.3742 9.52718 34.685 9.8042 34.9365C10.0812 35.1881 10.4069 35.3139 10.7812 35.3139H10.8936ZM20.125 33.8933V24.6594C20.125 24.2747 19.9827 23.9417 19.6982 23.6606C19.4137 23.3794 19.0768 23.2388 18.6875 23.2388C18.2982 23.2388 17.9613 23.3794 17.6768 23.6606C17.3923 23.9417 17.25 24.2747 17.25 24.6594V33.8933C17.25 34.278 17.3923 34.611 17.6768 34.8922C17.9613 35.1733 18.2982 35.3139 18.6875 35.3139C19.0768 35.3139 19.4137 35.1733 19.6982 34.8922C19.9827 34.611 20.125 34.278 20.125 33.8933ZM28.75 33.8933V24.6594C28.75 24.2747 28.6077 23.9417 28.3232 23.6606C28.0387 23.3794 27.7018 23.2388 27.3125 23.2388C26.9232 23.2388 26.5863 23.3794 26.3018 23.6606C26.0173 23.9417 25.875 24.2747 25.875 24.6594V33.8933C25.875 34.278 26.0173 34.611 26.3018 34.8922C26.5863 35.1733 26.9232 35.3139 27.3125 35.3139C27.7018 35.3139 28.0387 35.1733 28.3232 34.8922C28.6077 34.611 28.75 34.278 28.75 33.8933ZM36.6562 34.0043L37.375 24.7704C37.4049 24.3857 37.2889 24.0416 37.0269 23.7382C36.7648 23.4349 36.4391 23.2684 36.0498 23.2388C35.6605 23.2092 35.3123 23.3239 35.0054 23.5829C34.6984 23.8418 34.5299 24.1637 34.5 24.5484L33.7812 33.7823C33.7513 34.1671 33.8674 34.5111 34.1294 34.8145C34.3914 35.1178 34.7171 35.2843 35.1064 35.3139H35.2188C35.5931 35.3139 35.9188 35.1881 36.1958 34.9365C36.4728 34.685 36.6263 34.3742 36.6562 34.0043ZM10.6914 6.99075L8.60254 16.1358H5.6377L7.90625 6.34704C8.19075 5.04483 8.8571 3.98308 9.90527 3.1618C10.9535 2.34052 12.1514 1.92987 13.499 1.92987H17.25C17.25 1.54513 17.3923 1.21218 17.6768 0.931017C17.9613 0.649857 18.2982 0.509277 18.6875 0.509277H27.3125C27.7018 0.509277 28.0387 0.649857 28.3232 0.931017C28.6077 1.21218 28.75 1.54513 28.75 1.92987H32.501C33.8486 1.92987 35.0466 2.34052 36.0947 3.1618C37.1429 3.98308 37.8092 5.04483 38.0938 6.34704L40.3623 16.1358H37.3975L35.3086 6.99075C35.1439 6.33964 34.8032 5.80692 34.2866 5.39258C33.77 4.97824 33.1748 4.77107 32.501 4.77107H28.75C28.75 5.15581 28.6077 5.48876 28.3232 5.76992C28.0387 6.05108 27.7018 6.19166 27.3125 6.19166H18.6875C18.2982 6.19166 17.9613 6.05108 17.6768 5.76992C17.3923 5.48876 17.25 5.15581 17.25 4.77107H13.499C12.8252 4.77107 12.23 4.97824 11.7134 5.39258C11.1968 5.80692 10.8561 6.33964 10.6914 6.99075Z" fill="white"/>
                  </svg>
                </a>
              </div>
            </div>
      </nav>
    </header>


    <!-- ОТКРЫТОЕ МЕНЮ МОБИЛЬНОЙ ВЕРСИИ -->
    <div v-if="visibleMenu" class="z-10 fixed bg-white h-full w-full text-[20px] flex flex-col items-start p-6 pl-10 overflow-y-scroll">

      <button v-on:click="visibleMenu=!visibleMenu" class="self-end">
        <svg   width="21" height="21" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M17.564 2.0638C17.6709 1.95704 17.7558 1.83026 17.8137 1.69072C17.8716 1.55117 17.9014 1.40159 17.9015 1.25051C17.9016 1.09943 17.8719 0.949809 17.8142 0.810193C17.7565 0.670577 17.6718 0.543698 17.565 0.436802C17.4583 0.329906 17.3315 0.245086 17.192 0.187184C17.0524 0.129282 16.9028 0.0994328 16.7518 0.09934C16.6007 0.0992471 16.4511 0.128913 16.3114 0.186643C16.1718 0.244374 16.0449 0.329038 15.938 0.435802L9.00005 7.3738L2.06405 0.435802C1.84816 0.219916 1.55536 0.0986328 1.25005 0.0986328C0.944738 0.0986328 0.651933 0.219916 0.436047 0.435802C0.22016 0.651689 0.098877 0.944493 0.098877 1.2498C0.098877 1.55511 0.22016 1.84792 0.436047 2.0638L7.37405 8.9998L0.436047 15.9358C0.329151 16.0427 0.244356 16.1696 0.186504 16.3093C0.128653 16.4489 0.098877 16.5986 0.098877 16.7498C0.098877 16.901 0.128653 17.0507 0.186504 17.1903C0.244356 17.33 0.329151 17.4569 0.436047 17.5638C0.651933 17.7797 0.944737 17.901 1.25005 17.901C1.40122 17.901 1.55091 17.8712 1.69058 17.8133C1.83025 17.7555 1.95715 17.6707 2.06405 17.5638L9.00005 10.6258L15.938 17.5638C16.1539 17.7794 16.4466 17.9005 16.7518 17.9003C17.0569 17.9001 17.3494 17.7787 17.565 17.5628C17.7807 17.3469 17.9017 17.0542 17.9015 16.7491C17.9013 16.444 17.7799 16.1514 17.564 15.9358L10.626 8.9998L17.564 2.0638Z" fill="black"/>
        </svg>
      </button>


        <p class="text-[24px] mt-8 mb-3">
          +7(915)111-11-11
        </p>

        <p class="mb-3">
          <router-link to="/login" class="mr-3" v-on:click="visibleMenu=!visibleMenu">
            Вход | 
          </router-link>
          
          <router-link to="/register" class="mr-3" v-on:click="visibleMenu=!visibleMenu">
            Регистрация
          </router-link>
        </p>

        <router-link to="/" class="mb-3" v-on:click="visibleMenu=!visibleMenu">
            Главная
        </router-link>


        <div class="flex mb-3">
              <p class="mr-3">
                Каталог
              </p>

              <button v-on:click="visibleCatalog=!visibleCatalog">

                <svg v-if="!visibleCatalog" width="22px" height="22px" viewBox="0 0 18 12" fill="black" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 11.1L0 2.1L2.1 0L9 6.9L15.9 0L18 2.1L9 11.1Z" fill="black"/>
                </svg>

                <svg v-if="visibleCatalog" width="22px" height="22px" viewBox="0 0 18 12" fill="black" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.115 11.115L9 4.245L15.885 11.115L18 9L9 0L0 9L2.115 11.115Z" fill="black"/>
                </svg>
                
              </button>
        </div>
        <div v-if="visibleCatalog" class="flex flex-col items-start mb-8 ml-6">
              <a v-on:click="setCategory(1);visibleMenu=!visibleMenu" class="mb-2">
                Гитары
              </a>
              <a v-on:click="setCategory(2);visibleMenu=!visibleMenu" class="mb-2">
                Укулеле
              </a>
              <a v-on:click="setCategory(3);visibleMenu=!visibleMenu" class="mb-2">
                Клавишные инструменты
              </a>
              <a v-on:click="setCategory(4);visibleMenu=!visibleMenu" class="mb-2">
                Ударные инструменты
              </a>
              <a v-on:click="setCategory(5);visibleMenu=!visibleMenu" class="mb-2">
                Духовые инструменты
              </a>
              <a v-on:click="setCategory(6);visibleMenu=!visibleMenu" class="mb-2">
                Аккордеоны, баяны, гармони
              </a>

          </div>



        <p class="mb-3">
          Доставка и оплата
        </p>

        <router-link to="/blog" class="mr-3" v-on:click="visibleMenu=!visibleMenu">
          Блог
        </router-link>

    </div>








    <main class="mb-auto">
      <router-view/>
    </main>
    













    <footer class="h-80 bg-gradient-to-t from-[#220000] to-[#580005] to-43.47% flex justify-between p-12 hidden lg:flex">
      <div class="flex flex-col justify-between">
        <div class="w-[250px] mr-32">
            <router-link to="/" class="block ">
              <img src="./assets/logo.png" alt="Логотип" class=" block h-24 w-[100px]">
            </router-link>
        </div>

        <p class="text-white text-[20px]">
          +7(915)111-11-11
        </p>

        <div class="flex justify-between w-[350px] ">
          <img src="./assets/tg.png" alt="Телеграм" class="h-[60px]">

          <img src="./assets/vk.png" alt="Вконтакте" class="h-[60px]">

          <img src="./assets/whatsapp.png" alt="ВатсАпп" class="h-[60px]">
        </div>
      </div>

      <div class="flex text-white text-[20px]">
        <div class="flex flex-col mr-32">
          <p class="mb-6 text-[24px] font-medium">
            Покупателям
          </p>
          <p class="mb-2">
            Где мой заказ?
          </p>
          <p class="mb-2">
            Горячая линия
          </p>
          <p class="mb-2">
            Как сделать заказ
          </p>
          <p class="mb-2">
            Покупка в кредит
          </p>
          <p>
            Гарантия
          </p>

        </div>

        <div class="flex flex-col">
          <p class="mb-6 text-[24px] font-medium">
            Сотрудничество
          </p>
          <p class="mb-2">
            Поставщикам
          </p>
          <p class="mb-2">
            Дилерам
          </p>
          <p>
            Арендодателям
          </p>
        </div>
      </div>

    </footer>


    <!-- МОБИЛЬНАЯ ВЕРСИЯ FOOTER -->
    <footer class="text-white text-[16px] min-h-80 bg-gradient-to-t from-[#220000] to-[#580005] to-43.47% flex flex-col items-items- justify-between p-12 lg:hidden">

          <div class="mb-8">
            <div class="flex mb-6 mr-6">
              <p class="text-[18px] font-medium">
                Покупателям
              </p>

              <button v-on:click="visible=!visible">

                <svg v-if="!visible" width="28px" height="24px" viewBox="0 0 18 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 11.1L0 2.1L2.1 0L9 6.9L15.9 0L18 2.1L9 11.1Z" fill="white"/>
                </svg>

                <svg v-if="visible" width="28px" height="24px" viewBox="0 0 18 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.115 11.115L9 4.245L15.885 11.115L18 9L9 0L0 9L2.115 11.115Z" fill="white"/>
                </svg>
                
              </button>
            </div>

            <div v-if="visible">
              <p class="mb-2">
                Где мой заказ?
              </p>
              <p class="mb-2">
                Горячая линия
              </p>
              <p class="mb-2">
                Как сделать заказ
              </p>
              <p class="mb-2">
                Покупка в кредит
              </p>
              <p>
                Гарантия
              </p>
            </div>
          </div>


        <div class="mb-8">
            <div class="flex mb-6 mr-6">
              <p class="text-[18px] font-medium">
                Сотрудничество
              </p>

              <button v-on:click="visibleSotrud=!visibleSotrud">

                <svg v-if="!visibleSotrud" width="28px" height="24px" viewBox="0 0 18 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 11.1L0 2.1L2.1 0L9 6.9L15.9 0L18 2.1L9 11.1Z" fill="white"/>
                </svg>

                <svg v-if="visibleSotrud" width="28px" height="24px" viewBox="0 0 18 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.115 11.115L9 4.245L15.885 11.115L18 9L9 0L0 9L2.115 11.115Z" fill="white"/>
                </svg>
                
              </button>
            </div>

            <div v-if="visibleSotrud">
              <p class="mb-2">
                Поставщикам
              </p>
              <p class="mb-2">
                Дилерам
              </p>
              <p>
                Арендодателям
              </p>
            </div>
          </div>




      <div class="flex justify-around">
          <img src="./assets/tg.png" alt="Телеграм" class="h-[50px] mr-4">

          <img src="./assets/vk.png" alt="Вконтакте" class="h-[50px] mr-4">

          <img src="./assets/whatsapp.png" alt="ВатсАпп" class="h-[50px] mr-4">
      </div>

    </footer>



  </div>
    
  </div>
</template>






<script>
import './assets/tailwind.css';

 export default {
  name: 'App',

  data: () => ({
      visible: false, 
      visibleSotrud: false,
      visibleCatalog: false,
      visibleMenu: false,
      visibleCatalogDesktop: false,
    }),

    methods: {
      updateVisibleCatalog() {
        this.visibleCatalogDesktop = false;
      },

      setCategory(cat) {
          this.selectCategory = cat;
          this.$router.push({ name: 'CatalogSection', params: { catalogcategory: this.selectCategory } })
          this.$store.dispatch('GET_INSTRUMENTS_FILTER_CATEGORY', cat);
          this.$store.dispatch('GET_SUBCATEGORY_FILTER_CATEGORY', cat);
      },
    }
 }


</script>
