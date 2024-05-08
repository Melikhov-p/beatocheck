<script setup>

</script>

<template>
  <div class="">
    <div class="text-center">
      <p class="text-md font-medium text-white border-b border-b-deep-ocean p-7">БЫСТРЫЕ ДЕЙСТВИЯ</p>
    </div>
    <div class="flex flex-col py-7 px-5 gap-5">
      <div class="flex flex-col">
        <div class="flex justify-center items-center">
          <span class="text-center text-ocean-breath">Загрузить</span>
        </div>
        <div class="grid grid-cols-3 gap-1 mt-2">
          <div class="flex relative p-0.5 rounded-md max-w-sm hover:bg-gradient-to-r hover:from-sky-500 hover:to-sky-700">
            <a class="w-full py-5 text-center bg-dark-submarine hover:bg-light-submarine hover:cursor-pointer hover:text-sky-700 rounded-md">
              БИТ
            </a>
          </div>
          <div class="flex relative p-0.5 rounded-md max-w-sm hover:bg-gradient-to-r hover:from-sky-800 hover:to-indigo-500">
            <a class="w-full py-5 text-center bg-dark-submarine hover:bg-light-submarine hover:cursor-pointer rounded-md hover:text-indigo-500">
              КИТ
            </a>
          </div>
          <div class="flex relative p-0.5 rounded-md max-w-sm hover:bg-gradient-to-r hover:from-indigo-600 hover:to-indigo-700">
            <a class="w-full py-5 text-center bg-dark-submarine hover:bg-light-submarine hover:cursor-pointer rounded-md hover:text-indigo-700">
              СЭМПЛ
            </a>
          </div>
        </div>
      </div>
      <div class="flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-red-600">
        <a class="w-full p-5 text-center bg-dark-submarine hover:bg-light-submarine hover:cursor-pointer rounded-md hover:text-red-400">
          Поддержка
          <img alt="add_product" src="/support.svg" class="absolute right-3 top-6 w-5" />
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>