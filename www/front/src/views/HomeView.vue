<script setup>
import TrackFiltersComp from '@/components/TrackFiltersComp.vue'
import ProductsListComp from '@/components/ProductsListComp.vue'
import SideMenuFastActionsComp from '@/components/SideMenuFastActionsComp.vue'
</script>

<template>
  <div class="flex gap-2">
    <div class="rounded text-white w-full">

      <TrackFiltersComp/>

      <ProductsListComp grid_cols="5"/>

    </div>
<!--    <div class="text-white w-1/5 bg-light-submarine rounded shadow-xl shadow-dark-submarine">-->
<!--      <SideMenuFastActionsComp/>-->
<!--    </div>-->
  </div>
</template>
