<script setup>

import ProductsListComp from '@/components/ProductsListComp.vue'
import { ref } from 'vue'

const subscribed = ref(false)

function subscribe() {
  subscribed.value = !subscribed.value
}
</script>

<template>
  <div class="flex py-10 text-white gap-4">
    <div class="w-1/4 h-full">
      <div class="bg-light-submarine rounded-lg p-5 h-full">
        <img src="/default_avatar.svg" class="w-full rounded-full" />
        <div class="pt-5">
          <h1 class="text-xl font-bold text-center">Имя</h1>
          <div class="flex justify-center mt-3">
            <div v-if="subscribed" class="flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-sky-700">
              <a class="w-full text-center p-2 bg-dark-submarine bg-opacity-75 rounded hover:cursor-pointer hover:bg-transparent font-medium" @click="subscribe()">Подписаться</a>
            </div>
            <div v-else class="flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-sky-700">
              <a class="w-full text-center p-2 bg-transparent rounded hover:cursor-pointer hover:bg-dark-submarine hover:bg-opacity-25 font-medium" @click="subscribe()">Вы подписаны</a>
            </div>
            <!--          <a class="border border-light-input-error bg-input-error text-text-error p-3 rounded hover:bg-light-input-error hover:text-light-text-error hover:cursor-pointer">Пожаловаться</a>-->
          </div>
        </div>
        <div class="pt-2 mt-5 border-t border-slate-500">
          <h1 class="text-slate-300 text-s">Информация</h1>
          <div class="flex flex-col gap-3 border-b pb-3 border-slate-500 pt-3">
            <div class="flex justify-between">
              <p class="text-slate-500">Подписчики</p>
              <p class="text-slate-300">1000</p>
            </div>
            <div class="flex justify-between">
              <p class="text-slate-500">Треков</p>
              <p class="text-slate-300">13</p>
            </div>
            <div class="flex justify-between">
              <p class="text-slate-500">Проигрываний</p>
              <p class="text-slate-300">1000</p>
            </div>
          </div>
        </div>
        <div class="mt-3 border-b border-slate-500 pb-3">
          <h1 class="text-slate-300 text-s">Обо мне</h1>
          <p class="text-slate-300 pt-3">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores aut dicta dolore, doloremque doloribus ducimus error illo ipsam neque nobis tempora voluptatibus voluptatum? Adipisci cum dicta maxime obcaecati vero voluptates.</p>
        </div>
        <div class="mt-3">
          <h1 class="text-slate-300 text-s">Ссылки</h1>
          <div class="flex flex-col pt-3">
            <a>VK</a>
            <a>VK</a>
          </div>
        </div>
      </div>
      <div class="bg-light-submarine rounded-lg p-5 h-full mt-5">
        <h1 class="text-xl font-bold text-center">Рекомендации</h1>
      </div>
    </div>
    <div class="w-3/4">
      <div class="w-full rounded-lg">
        <div class="flex justify-between">
          <div class="flex gap-5">
            <p class="text-slate-100 mb-5 pb-2 text-lg border-b border-slate-400 hover:border-slate-50 hover:cursor-pointer">Треки</p>
            <p class="text-slate-100 mb-5 pb-2 text-lg border-b border-slate-400 hover:border-slate-50 hover:cursor-pointer">Блог</p>
          </div>
        </div>
        <ProductsListComp grid_cols="4" />
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>