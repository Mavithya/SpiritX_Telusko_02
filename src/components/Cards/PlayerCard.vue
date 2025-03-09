<template>
  <div class="bg-white shadow-md rounded-lg p-4 flex flex-col items-center text-center transition-transform transform hover:scale-105">
    <img :src="player.image" :alt="player.name" class="w-24 h-24 rounded-full border-2 border-gray-300" />
    <h2 class="text-lg font-semibold mt-3">{{ player.name }}</h2>
    <p class="text-gray-600">{{ player.role }}</p>
    <span class="text-blue-500 font-medium">{{ player.team }}</span>
  </div>
</template>

<script>
export default {
  props: {
    player: Object,
  },
};
</script>
