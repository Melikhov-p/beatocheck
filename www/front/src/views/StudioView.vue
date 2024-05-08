<script setup>

</script>

<template>
  <div class="flex flex-col">
    <div class="bg-light-submarine text-white w-full mt-5 rounded">
      <div class="flex justify-between">
        <div class="flex gap-5 p-5">
          <a class="p-5 border-b border-dark-galaxy hover:bg-dark-submarine hover:border-deep-galaxy hover:cursor-pointer" href="/add_track">Добавить Бит</a>
          <a class="p-5 border-b border-dark-galaxy hover:bg-dark-submarine hover:border-deep-galaxy hover:cursor-pointer">Продвижение</a>
          <a class="p-5 border-b border-dark-galaxy hover:bg-dark-submarine hover:border-deep-galaxy hover:cursor-pointer">Статистика</a>
        </div>
      </div>
    </div>
    <RouterView/>
  </div>
</template>

<style scoped>

</style>