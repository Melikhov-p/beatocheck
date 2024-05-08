<script setup>
import ProductCardComp from '@/components/ProductCardComp.vue'

const products = [
  {
    'id': 1,
    'author': 'John Doe',
    'title': 'Product 1',
    'type': 'beat',
    'price': 100,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'image': '/lynxear_lynx_ear_logo_black_and_white_modern_67387d8f_2a17_4ea4.png',
    'discount_percent': 10,
    'genre': 'Hip-Hop',
    'bpm': 120,
    'total_price': 90,
  },
  {
    'id': 1,
    'author': 'John Doe',
    'title': 'Product 1',
    'type': 'beat',
    'price': 100,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'image': '/cover.jpeg',
    'discount_percent': 10,
    'genre': 'Hip-Hop',
    'bpm': 120,
    'total_price': 90,
  },
  {
    'id': 1,
    'author': 'John Doe',
    'title': 'Product 1',
    'type': 'beat',
    'price': 100,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'image': '/cover.jpeg',
    'discount_percent': 10,
    'genre': 'Hip-Hop',
    'bpm': 120,
    'total_price': 90,
  },
  {
    'id': 1,
    'author': 'John Doe',
    'title': 'Product 1',
    'type': 'beat',
    'price': 100,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'image': '/cover.jpeg',
    'discount_percent': 10,
    'genre': 'Hip-Hop',
    'bpm': 120,
    'total_price': 90,
  },
  {
    'id': 1,
    'author': 'John Doe',
    'title': 'Product 1',
    'type': 'beat',
    'price': 100,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'image': '/cover.jpeg',
    'discount_percent': 10,
    'genre': 'Hip-Hop',
    'bpm': 120,
    'total_price': 902,
  },
  {
    'id': 1,
    'author': 'John Doe',
    'title': 'Product 1',
    'type': 'beat',
    'price': 100,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'image': '/cover.jpeg',
    'discount_percent': 0,
    'genre': 'Hip-Hop',
    'bpm': 120,
    'total_price': 100,
  },
  {
    'id': 1,
    'author': 'John Doe',
    'title': 'Product 1',
    'type': 'beat',
    'price': 100,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'image': '/cover.jpeg',
    'discount_percent': 0,
    'genre': 'Hip-Hop',
    'bpm': 120,
    'total_price': 100,
  },
  {
    'id': 1,
    'author': 'John Doe',
    'title': 'Product 1',
    'type': 'beat',
    'price': 100,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'image': '/cover.jpeg',
    'discount_percent': 0,
    'genre': 'Hip-Hop',
    'bpm': 120,
    'total_price': 100,
  },
  {
    'id': 1,
    'author': 'John Doe',
    'title': 'Product 1',
    'type': 'beat',
    'price': 100,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'image': '/cover.jpeg',
    'discount_percent': 0,
    'genre': 'Hip-Hop',
    'bpm': 120,
    'total_price': 100,
  },
]
defineProps({
  grid_cols: String
})
</script>

<template>
  <div v-if="grid_cols" :class="'mb-5 grid sm:grid-cols-1 md:grid-cols-3 gap-5 xl:grid-cols-'+grid_cols">
    <ProductCardComp v-for="product in products" :key="product.id" :product="product"/>
  </div>
</template>

<style scoped>

</style>