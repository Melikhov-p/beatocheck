<script setup>
function checkPassword() {
  let password = document.getElementById('password')
  let confirm_password = document.getElementById('confirm_password')
  if (password.value == '' && confirm_password.value == ''){
    confirm_password.classList.remove('bg-input-error', 'text-text-error')
    document.getElementById('error-password').classList.add('hidden')
    return
  }
  if (password.value != confirm_password.value) {
    confirm_password.classList.add('bg-input-error', 'text-text-error')
    document.getElementById('error-password').classList.remove('hidden')
  } else {
    confirm_password.classList.remove('bg-input-error', 'text-text-error')
    confirm_password.classList.add('bg-input-light-success', 'text-light-success')
    password.classList.add('bg-input-light-success', 'text-light-success')
    document.getElementById('error-password').classList.add('hidden')
  }
}

function checkUsername() {
  let username = document.getElementById('username')
  const a = 'lynxear'
  if (username.value == a) {
    username.classList.add('bg-input-error', 'text-text-error')
    document.getElementById('error-username').classList.remove('hidden')
  } else {
    username.classList.remove('bg-input-error', 'text-text-error')
    username.classList.add('bg-input-light-success', 'text-light-success')
    document.getElementById('error-username').classList.add('hidden')
  }
}
</script>

<template>
  <div class="flex flex-col gap-5">
    <div class="w-full relative">
      <input type="text" class="rounded bg-light-submarine p-5 w-full outline-0 focus:bg-input-focus" placeholder="Логин" id="username" @change="checkUsername()" />
      <span class="absolute text-text-error z-20 right-5 top-1/3 hidden" id="error-username">Логин уже занят</span>
    </div>
    <input type="email" class="rounded bg-light-submarine p-5 w-full outline-0 focus:bg-input-focus" placeholder="E-Mail" />
    <input type="password" class="rounded bg-light-submarine p-5 w-full outline-0 focus:bg-input-focus" placeholder="Пароль" id="password" @change="checkPassword()" />
    <div class="w-full relative">
      <input type="password" class="rounded bg-light-submarine p-5 w-full outline-0 focus:bg-input-focus" placeholder="Повторите пароль" id="confirm_password" @change="checkPassword()" />
      <span class="absolute text-text-error z-20 right-5 top-1/3 hidden" id="error-password">Пароли не совпадают</span>
    </div>
    <input type="submit" value="Регистрация" class="rounded mt-5 p-5 border border-input-light-success bg-input-dark-success text-dark-success hover:bg-input-light-success hover:text-light-success hover:cursor-pointer" />
  </div>

</template>

<style scoped>

</style>