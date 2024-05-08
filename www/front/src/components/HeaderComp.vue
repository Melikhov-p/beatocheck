<script setup>
const user = false
</script>

<template>
  <!--  bg-[#0c111d]-->
  <header class="bg-dark-submarine text-white px-28 pt-8 border-b border-deep-ocean">
    <div class="flex justify-between">
      <div class="flex flex-col">
        <div class="flex gap-3 items-center">
          <div>
            <a href="/">
              <p class="text-2xl font-extrabold scale-y-150">BEATOCHECK</p>
            </a>
          </div>
          <div class="flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-sky-700 to-indigo-700">
            <img alt="search" src="/search.svg" class="absolute left-3 top-3" />
            <input placeholder="Поиск..." class=" bg-input-disabled focus:bg-input-focus border-gray-900 rounded-l-md py-2 pl-10 pr-4 outline-0 w-80" />
            <div class="bg-input-focus hover:cursor-pointer flex items-center hover:bg-indigo-800 rounded-r px-3">
              <span class="">Найти</span>
            </div>
          </div>
        </div>
        <div class="mt-8">
          <ul class="flex items-center gap-10">
            <li class="pb-1 border-b border-b-dark-submarine text-slate-300 hover:border-light-galaxy hover:cursor-pointer hover:text-slate-50">Маркет</li>
            <li class="pb-1 border-b border-b-dark-submarine text-slate-300 hover:border-light-galaxy hover:cursor-pointer hover:text-slate-50">Битмейкеры</li>
            <li class="pb-1 border-b border-b-dark-submarine text-slate-300 hover:border-light-galaxy hover:cursor-pointer hover:text-slate-50">Новости</li>
          </ul>
        </div>
      </div>
      <div class="flex flex-col justify-around">
        <div class="flex items-center gap-2">
          <div class="flex flex-col ">
            <img alt="cart" src="/cart.svg" class="hover:scale-105 hover:cursor-pointer" />
          </div>
          <div class="flex flex-col">
            <!--          <div class="rounded-full max-w-sm w-avatar-big bg-gradient-to-r from-sky-700 to-indigo-700 p-0.5">-->
            <!--            <img alt="user" src="/default_avatar.svg" class="w-avatar-big rounded-full bg-input-disabled" />-->
            <!--          </div>-->
            <div class="flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-sky-700">
              <a v-if="user" class="p-1 text-center bg-dark-submarine font-light rounded hover:cursor-pointer hover:bg-transparent">Username</a>
              <a v-else class="p-1 text-center bg-dark-submarine font-light rounded hover:cursor-pointer hover:bg-transparent" href="/auth">Войти</a>
            </div>
          </div>
        </div>
        <div>
          <div class="flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-sky-700">
            <a href="/studio" class="w-full text-center p-1 bg-dark-submarine font-light rounded hover:cursor-pointer hover:bg-transparent">Студия</a>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>

</style>