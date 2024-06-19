<script setup>

</script>

<template>
  <div class="w-full rounded mt-5">
    <div class="py-5 flex flex-col">
      <div class="flex justify-between">
        <div class="flex gap-5 flex-col w-3/5 text-white">
          <input type="text" class="rounded bg-light-submarine p-5 w-full outline-0 focus:bg-input-focus" placeholder="Название" />
          <div class="flex gap-5">
            <input type="text" class="rounded bg-light-submarine p-5 w-full outline-0 focus:bg-input-focus" placeholder="BPM" />
            <select id="genre_select" class="block p-2 w-full text-slate-400 text-lg bg-light-submarine focus:bg-input-focus  border-light-galaxy rounded focus:outline-none peer">
              <option value="US" selected>Тональность</option>
              <option value="US">C</option>
              <option value="CA">D</option>
              <option value="FR">E</option>
              <option value="DE">F</option>
              <option value="DE">G</option>
              <option value="DE">A</option>
              <option value="DE">B</option>
            </select>
            <select id="genre_select" class="block p-2 w-full text-slate-400 text-lg bg-light-submarine focus:bg-input-focus  border-light-galaxy rounded focus:outline-none peer">
              <option value="US" selected>Жанр</option>
              <option value="US">Hip-Hop</option>
              <option value="CA">Pop</option>
              <option value="FR">Rap</option>
              <option value="DE">Trap</option>
            </select>
          </div>
          <input type="text" class="rounded bg-light-submarine p-5 w-full outline-0 focus:bg-input-focus" placeholder="Теги через запятую" />
          <div class="flex gap-5">
            <div class="w-full flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-sky-700">
              <label for="mp3" class="w-full text-center p-5 rounded bg-dark-submarine bg-opacity-75 hover:cursor-pointer hover:bg-transparent font-medium">Добавить MP3</label>
              <input type="file" class="hidden" ref="image" id="mp3" accept="audio/*" />
            </div>
            <div class="w-full flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-sky-700">
              <label for="wav" class="w-full text-center p-5 rounded bg-dark-submarine bg-opacity-75 hover:cursor-pointer hover:bg-transparent font-medium">Добавить WAV</label>
              <input type="file" class="hidden" ref="image" id="wav" accept="audio/*" />
            </div>
            <div class="w-full flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-sky-700">
              <label for="trackout" class="w-full text-center p-5 rounded bg-dark-submarine bg-opacity-75 hover:cursor-pointer hover:bg-transparent font-medium">Добавить Trackout</label>
              <input type="file" class="hidden" ref="image" id="trackout" accept="audio/*" />
            </div>
          </div>
          <div class="w-full text-white">
            <h1 class="font-medium text-xl">Лицензии</h1>
            <div class="flex gap-5 mt-5">
              <div class="rounded bg-light-submarine p-5 flex flex-col gap-5">
                <h1>MP3 Аренда</h1>
                <div class="relative">
                  <input type="text" class="bg-input-disabled p-5 outline-0 focus:bg-input-focus" placeholder="Цена" />
                  <span class="absolute text-xl z-20 right-5 top-4">₽</span>
                </div>
              </div>
              <div class="rounded bg-light-submarine p-5 flex flex-col gap-5">
                <h1>WAV Аренда</h1>
                <div class="relative">
                  <input type="text" class="bg-input-disabled p-5 outline-0 focus:bg-input-focus" placeholder="Цена" />
                  <span class="absolute text-xl z-20 right-5 top-4">₽</span>
                </div>
              </div>
              <div class="rounded bg-light-submarine p-5 flex flex-col gap-5">
                <h1>Полные права</h1>
                <div class="relative">
                  <input type="text" class="bg-input-disabled p-5 outline-0 focus:bg-input-focus" placeholder="Цена" />
                  <span class="absolute text-xl z-20 right-5 top-4">₽</span>
                </div>
              </div>
            </div>
          </div>
          <input type="submit" value="Загрузить" class="mt-5 p-5 border border-input-light-success bg-input-dark-success text-dark-success hover:bg-input-light-success hover:text-light-success hover:cursor-pointer" />
        </div>
        <div class=" w-1/3 h-1/3 flex-col">
          <div class="bg-grey-blue rounded">
            <img src="/cover.jpeg" />
          </div>
          <div class="flex justify-center mt-5">
            <div class="w-full flex relative p-0.5 rounded-md max-w-sm bg-gradient-to-r from-indigo-700 to-sky-700">
              <label for="wav" class="w-full text-center p-5 rounded bg-dark-submarine bg-opacity-75 hover:cursor-pointer hover:bg-transparent text-white font-medium">Выбрать обложку</label>
              <input type="file" class="hidden" ref="image" id="wav" accept="audio/*" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>