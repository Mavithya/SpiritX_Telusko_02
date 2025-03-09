<template>
  <div class="relative flex flex-col w-full min-w-0 mb-6 break-words bg-white rounded shadow-lg">
    <div class="block w-full p-4 overflow-x-auto">
      <div class="flex justify-center">
        <!-- Player Card -->
        <div class="flex flex-col items-center p-4 bg-white rounded-lg shadow-md">
          <img src="DashBoard Images\1.png" alt="Player" class="w-24 h-24 mb-4 rounded-full">
          <h4 class="font-semibold text-blueGray-700">Player Name</h4>
          <p class="text-sm text-blueGray-500">83 Rating</p>
          <p class="text-sm text-blueGray-500">Spain</p>
          <div class="w-full mt-2">
            <div class="flex justify-between text-sm text-blueGray-500">
              <span>Strength</span>
              <span>Speed</span>
            </div>
            <div class="flex justify-between mt-1">
              <div class="w-1/2 h-2 bg-red-200 rounded">
                <div class="h-2 bg-red-500 rounded" style="width: 60%;"></div>
              </div>
              <div class="w-1/2 h-2 ml-2 bg-blue-200 rounded">
                <div class="h-2 bg-blue-500 rounded" style="width: 40%;"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-center p-4">
      <button
        class="px-3 py-1 text-xs font-bold text-white uppercase transition-all duration-150 ease-linear bg-indigo-500 rounded outline-none active:bg-indigo-600 focus:outline-none"
        type="button"
      >
        See all
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PlayerCard',
};
</script>

<style scoped>
/* Add any custom styles here if needed */
</style>