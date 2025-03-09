<template>
  <div
    class="relative flex flex-col w-full min-w-0 mt-16 mb-6 break-words bg-white rounded-lg shadow-xl"
  >
    <div class="px-6">
      <div class="flex flex-wrap justify-center">
        <div class="flex justify-center w-full px-4">
          <div class="relative">
            <img
              alt="..."
              :src="team2"
              class="absolute h-auto -m-16 -ml-20 align-middle border-none rounded-full shadow-xl lg:-ml-16 max-w-150-px"
            />
          </div>
        </div>
        <div class="w-full px-4 mt-20 text-center">
          <div class="flex justify-center py-4 pt-8 lg:pt-4">
            <div class="p-3 mr-4 text-center">
              <span
                class="block text-xl font-bold tracking-wide uppercase text-blueGray-600"
              >
                22
              </span>
              <span class="text-sm text-blueGray-400">Friends</span>
            </div>
            <div class="p-3 mr-4 text-center">
              <span
                class="block text-xl font-bold tracking-wide uppercase text-blueGray-600"
              >
                10
              </span>
              <span class="text-sm text-blueGray-400">Photos</span>
            </div>
            <div class="p-3 text-center lg:mr-4">
              <span
                class="block text-xl font-bold tracking-wide uppercase text-blueGray-600"
              >
                89
              </span>
              <span class="text-sm text-blueGray-400">Comments</span>
            </div>
          </div>
        </div>
      </div>
      <div class="mt-12 text-center">
        <h3
          class="mb-2 text-xl font-semibold leading-normal text-blueGray-700"
        >
        Angelo Jayawardene
        </h3>
        <div
          class="mt-0 mb-2 text-sm font-bold leading-normal uppercase text-blueGray-400"
        >
          <i class="mr-2 text-lg fas fa-map-marker-alt text-blueGray-400"></i>
          Galle , Sri Lanka
        </div>
        <div class="mt-10 mb-2 text-blueGray-600">
          <i class="mr-2 text-lg fas fa-briefcase text-blueGray-400"></i>
          Left Handed Batsman
        </div>
        <div class="mb-2 text-blueGray-600">
          <i class="mr-2 text-lg fas fa-university text-blueGray-400"></i>
          University of Colombo
        </div>
      </div>
      <div class="py-10 mt-10 text-center border-t border-blueGray-200">
        <div class="flex flex-wrap justify-center">
          <div class="w-full px-4 lg:w-9/12">
            <p class="mb-4 text-lg leading-relaxed text-blueGray-700">
              
            </p>
            <a href="javascript:void(0);" class="font-normal text-emerald-500">
              Show more
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import team2 from "@/assets/img/team-2-800x800.jpg";

export default {
  data() {
    return {
      team2,
    };
  },
};
</script>
