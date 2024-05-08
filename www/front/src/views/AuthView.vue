<script setup>

import { ref } from 'vue'
import LoginComp from '@/components/LoginComp.vue'
import RegisterComp from '@/components/RegisterComp.vue'

const haveAccount = ref(true)

function switchUl(id) {
  if (id === 'ha') {
    haveAccount.value = true
    document.getElementById('dha').classList.remove('text-dark-galaxy', 'border-b', 'border-dark-galaxy')
    document.getElementById('ha').classList.add('text-dark-galaxy', 'border-b', 'border-dark-galaxy')
  }
  else {
    haveAccount.value = false
    document.getElementById('ha').classList.remove('text-dark-galaxy', 'border-b', 'border-dark-galaxy')
    document.getElementById('dha').classList.add('text-dark-galaxy', 'border-b', 'border-dark-galaxy')
  }
}
</script>

<template>
  <div class="flex justify-around text-white w-full my-5">
    <div class="rounded bg-dark-submarine p-5 w-2/3">
      <div class="mb-10">
        <ul class="flex gap-5 pt-10">
          <li class="text-dark-galaxy border-b border-dark-galaxy pb-1 hover:cursor-pointer" id="ha" @click="switchUl('ha')">У меня есть аккаунт</li>
          <li class="pb-1 hover:cursor-pointer" id="dha" @click="switchUl('dha')">У меня нет аккаунта</li>
        </ul>
      </div>
      <LoginComp v-if="haveAccount" />
      <RegisterComp v-else />
    </div>
  </div>
</template>

<style scoped>

</style>