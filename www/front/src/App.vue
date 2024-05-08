<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HeaderComp from '@/components/HeaderComp.vue'
import BannerComp from '@/components/BannerComp.vue'
import FooterComp from '@/components/FooterComp.vue'
</script>

<template>
  <div class="">
    <HeaderComp />

    <!--  <BannerComp/>-->

    <div class="px-28">
      <RouterView />
    </div>
  </div>

  <FooterComp />
</template>
<style scoped>
</style>
