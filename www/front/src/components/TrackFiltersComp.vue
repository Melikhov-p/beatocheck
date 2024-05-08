<script setup>

</script>

<template>
  <div class="pt-10 pb-3 flex gap-5 justify-between">
    <div class="flex items-center gap-5">
      <div>
        <select id="genre_select" class="block p-2 w-full text-white text-lg bg-light-submarine focus:bg-input-focus  border-light-galaxy rounded focus:outline-none peer">
          <option value="US" selected>Жанр</option>
          <option value="US">Hip-Hop</option>
          <option value="CA">Pop</option>
          <option value="FR">Rap</option>
          <option value="DE">Trap</option>
        </select>
      </div>
      <div>
        <select id="genre_select" class="block p-2 w-full text-white text-lg bg-light-submarine focus:bg-input-focus  border-light-galaxy rounded focus:outline-none peer">
          <option value="US" selected>BPM</option>
          <option value="US">Любой</option>
          <option value="US">50-75</option>
          <option value="CA">75-100</option>
          <option value="FR">100-125</option>
          <option value="DE">125-150</option>
          <option value="DE">150+</option>
        </select>
      </div>
      <div>
        <span>Цена от </span>
        <input type="text" placeholder="0" id="start_price" class="w-20 text-center p-2 text-sm text-white bg-transparent border-b border-light-galaxy focus:outline-none focus:border-sky-700 peer" />
        <span> до </span>
        <input type="text" placeholder="10000" id="end_price" class="w-20 text-center p-2 text-sm text-white bg-transparent border-b border-light-galaxy focus:outline-none focus:border-sky-700 peer" />
      </div>
    </div>
    <div>
      <div class="flex items-center gap-1">
        <span>Сначала</span>
        <div class="flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-indigo-400">
          <select id="genre_select" class="block text-center p-2 w-full text-white text-lg bg-light-submarine focus:bg-input-focus  border-light-galaxy rounded focus:bg-input-focus focus:outline-none peer">
            <option value="US" selected>Новые</option>
            <option value="US">Дорогие</option>
            <option value="US">Дешевые</option>
            <option value="CA">Со скидкой</option>
          </select>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>