<script setup>
import { ref } from 'vue'

function SelectLicense(id) {
  for(let i = 1; i <= 3; i++) {
    document.getElementById(`license-${i}`).classList.remove('bg-deep-ocean')
  }
  document.getElementById(id).classList.add('bg-deep-ocean')
}

</script>

<template>
  <div class="flex py-10 text-white gap-4">
    <div class="w-1/4 bg-light-submarine rounded-lg p-5">
      <div>
        <img alt="cover" src="/cover.jpeg" class="w-full rounded-lg" />
      </div>
      <div class="py-5">
        <h1 class="text-xl font-bold text-center">BEAT NAME</h1>
        <p class="text-center text-slate-300">Автор</p>
      </div>
      <div class="flex justify-around border-b pb-5 border-slate-500">
        <img src="/heart.svg" class="w-8 hover:scale-105 hover:cursor-pointer" />
        <img src="/link.svg" class="w-12 hover:scale-105 hover:cursor-pointer" />
      </div>
      <div class="pb-5">
        <p class="text-slate-500 pb-5 pt-2">Информация</p>
        <div class="flex flex-col gap-3 border-b pb-3 border-slate-500">
          <div class="flex justify-between">
            <p class="text-slate-500">Опубликован</p>
            <p class="text-slate-300">24.04.2024</p>
          </div>
          <div class="flex justify-between">
            <p class="text-slate-500">BPM</p>
            <p class="text-slate-300">120</p>
          </div>
          <div class="flex justify-between">
            <p class="text-slate-500">Тональность</p>
            <p class="text-slate-300">Gm</p>
          </div>
        </div>
      </div>
      <div class="pb-3 border-b border-slate-500">
        <p class="text-slate-500 pb-3">Теги</p>
        <div class="flex gap-3">
          <div class="rounded-lg bg-dark-submarine hover:bg-deep-ocean hover:cursor-pointer">
            <p class="text-slate-300 py-2 px-4">#Hip-Hop</p>
          </div>
          <div class="rounded-lg bg-dark-submarine hover:bg-deep-ocean hover:cursor-pointer">
            <p class="text-slate-300 py-2 px-4">#Rap</p>
          </div>
          <div class="rounded-lg bg-dark-submarine hover:bg-deep-ocean hover:cursor-pointer">
            <p class="text-slate-300 py-2 px-4">#Fire</p>
          </div>
        </div>
      </div>
      <div class="pt-2">
        <p class="text-slate-500 pb-3">Описание</p>
        <p class="text-slate-300">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam amet at doloremque dolores eligendi ex expedita incidunt ipsa molestiae mollitia, nemo nostrum pariatur quaerat quidem rem saepe similique veniam voluptate.</p>
      </div>
    </div>
    <div class="w-3/4 flex flex-col gap-4">
      <div class="w-full rounded-3xl bg-light-submarine p-5">
        BEAT PLAYER
      </div>
      <div class="w-full rounded-lg bg-light-submarine p-5">
        <div class="border-b border-dark-galaxy pb-5 flex justify-between items-center">
          <h1 class="text-lg font-light text-slate-300">Тип лицензии</h1>
          <div class="flex items-center gap-3">
            <div class="flex flex-col items-center">
              <span class="text-2xl text-slate-50">₽100</span>
            </div>
            <div>
              <a class="px-2 py-3.5 rounded border border-input-light-success bg-input-dark-success text-dark-success hover:bg-input-light-success hover:text-light-success hover:cursor-pointer">Добавить в корзину</a>
            </div>
          </div>
        </div>
        <div class="grid grid-cols-3 gap-4 pt-5">
          <div class="rounded-lg p-5 bg-dark-submarine hover:bg-deep-ocean hover:cursor-pointer flex flex-col pb-10" id="license-1" @click="SelectLicense('license-1')">
            <div>
              <h1 class="text-lg font-bold text-white">Аренда MP3</h1>
            </div>
            <div class="mt-3 flex gap-5">
              <p>₽100</p>
              <p class="text-slate-500">MP3</p>
            </div>
          </div>
          <div class="rounded-lg p-5 bg-dark-submarine hover:bg-deep-ocean hover:cursor-pointer flex flex-col pb-10" id="license-2" @click="SelectLicense('license-2')">
            <div>
              <h1 class="text-lg font-bold text-white">Аренда WAV</h1>
            </div>
            <div class="mt-3 flex gap-5">
              <p>₽500</p>
              <p class="text-slate-500">WAV</p>
            </div>
          </div>
          <div class="rounded-lg p-5 bg-dark-submarine hover:bg-deep-ocean hover:cursor-pointer flex flex-col pb-10" id="license-3" @click="SelectLicense('license-3')">
            <div>
              <h1 class="text-lg font-bold text-white">Полные права</h1>
            </div>
            <div class="mt-3 flex gap-5">
              <p>₽1000</p>
              <p class="text-slate-500">Trackout</p>
            </div>
          </div>
        </div>
      </div>
      <div class="w-full rounded-lg bg-light-submarine p-5">
        <h1 class="text-xl mb-5">Комментарии</h1>
        <div class="flex flex-col gap-3">
          <div class="flex p-3 bg-dark-submarine rounded-lg items-center gap-5">
            <div class="">
              <img src="/default_avatar.svg" class="w-avatar-big rounded-full" />
            </div>
            <div>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab aliquam amet assumenda consectetur consequuntur doloribus ducimus eaque esse fugit, harum hic impedit magnam, necessitatibus praesentium qui, saepe tempore. Dolor, ratione!</p>
            </div>
          </div>
          <div class="flex p-3 bg-dark-submarine rounded-lg items-center gap-5">
            <div class="">
              <img src="/default_avatar.svg" class="w-avatar-big rounded-full" />
            </div>
            <div>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab aliquam amet assumenda consectetur consequuntur doloribus ducimus eaque esse fugit, harum hic impedit magnam, necessitatibus praesentium qui, saepe tempore. Dolor, ratione!</p>
            </div>
          </div>
          <div class="flex p-3 bg-dark-submarine rounded-lg items-center gap-5">
            <div class="">
              <img src="/default_avatar.svg" class="w-avatar-big rounded-full" />
            </div>
            <div>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab aliquam amet assumenda consectetur consequuntur doloribus ducimus eaque esse fugit, harum hic impedit magnam, necessitatibus praesentium qui, saepe tempore. Dolor, ratione!</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>