<script setup>
defineProps({
  product: Object
})
</script>

<template>
  <div class="relative
  p-3
  flex
  flex-col
  border-deep-ocean
  rounded-lg
  hover:shadow-xl
  hover:shadow-dark-submarine
  transition
  hover:cursor-pointer
  hover:bg-light-submarine">
    <div class="relative">
      <div class="absolute top-0 left-0 w-full h-full flex opacity-0 hover:opacity-100 justify-center items-center">
        <div class="p-5 rounded-full bg-dark-submarine bg-opacity-35 hover:bg-opacity-85 hover:cursor-pointer">
          <img src="/play-button.svg" class="w-10"/>
        </div>
      </div>
      <img :src="product.image" class="w-full rounded-lg" />
    </div>
    <div class="pt-2 flex gap-2 items-center">
      <div v-if="product.discount_percent > 0">
        <span class="py-1 rounded font-light text-ocean-breath w-fit">₽{{ product.total_price }}</span>
        •
        <span class="font-light text-xs text-black bg-sunrise-yellow rounded p-1" :title="'-' + product.discount_percent + '%'"> SALE </span>
      </div>

      <span v-else class="py-1 py-0 rounded text-ocean-breath font-light  w-fit ">₽{{ product.total_price }} </span>
      •
      <span class="text-slate-400 font-light">{{ product.bpm }} BPM</span>
    </div>
    <div class=" pt-2">
      <a class="text-white font-bold hover:underline" :href="'/beat/' + product.id">{{ product.title }}</a>
    </div>
    <div class="py-2 flex items-center justify-between">
      <div class="flex items-center">
        <img src="/default_avatar.svg" class="rounded-full w-avatar-sm mr-2" />
        <a class="text-slate-400 font-light hover:underline" :href="'/@' + product.author">{{ product.author }}</a>
      </div>
      <div class="flex gap-2">
        <img src="/heart.svg" class="w-6 rounded-full hover:scale-105" />
        <img src="/plus.svg" class="w-12 rounded-full bg-grey-blue hover:scale-105 hover:bg-slate-600" />
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>