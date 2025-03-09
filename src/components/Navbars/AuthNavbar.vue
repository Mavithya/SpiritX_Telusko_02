<template>
  <nav class="absolute top-0 z-50 flex flex-wrap items-center justify-between w-full px-2 py-3 navbar-expand-lg">
    <div class="container flex flex-wrap items-center justify-between px-1 mx-auto">
      <div class="relative flex justify-between w-full lg:w-auto lg:static lg:block lg:justify-start">
        <router-link
          class="inline-block py-3 mr-4 font-bold leading-relaxed text-white uppercase text-md whitespace-nowrap"
          to="/">
          Cricket 11
        </router-link>
        <button
          class="block px-3 py-1 text-xl leading-none bg-transparent border border-transparent border-solid rounded outline-none cursor-pointer lg:hidden focus:outline-none"
          type="button" v-on:click="setNavbarOpen">
          <i class="text-white fas fa-bars"></i>
        </button>
      </div>
      <div class="items-center flex-grow bg-white lg:flex lg:bg-opacity-0 lg:shadow-none"
        :class="[navbarOpen ? 'block rounded shadow-lg' : 'hidden']" id="example-navbar-warning">
        <ul class="flex flex-col mr-auto list-none lg:flex-row">
     
          <li class="flex items-center">
            <PagesDropdown />
          </li>
        </ul>
        <ul class="flex flex-col list-none lg:flex-row lg:ml-auto">
        
          <li class="flex items-center">
            <a class="flex items-center px-3 py-4 text-xs font-bold uppercase lg:text-white lg:hover:text-blueGray-200 text-blueGray-700 lg:py-2"
              href="https://www.facebook.com/"
              target="_blank">
              <i class="text-lg lg:text-blueGray-200 text-blueGray-400 fab fa-facebook leading-lg" />
              <span class="inline-block ml-2 lg:hidden">Share</span>
            </a>
          </li>

          <li class="flex items-center">
            <a class="flex items-center px-3 py-4 text-xs font-bold uppercase lg:text-white lg:hover:text-blueGray-200 text-blueGray-700 lg:py-2"
              href="https://twitter.com/"
              target="_blank">
              <i class="text-lg lg:text-blueGray-200 text-blueGray-400 fab fa-twitter leading-lg" />
              <span class="inline-block ml-2 lg:hidden">Tweet</span>
            </a>
          </li>

          <li class="flex items-center">
            <a class="flex items-center px-3 py-4 text-xs font-bold uppercase lg:text-white lg:hover:text-blueGray-200 text-blueGray-700 lg:py-2"
              href="https://github.com/" target="_blank">
              <i class="text-lg lg:text-blueGray-200 text-blueGray-400 fab fa-github leading-lg" />
              <span class="inline-block ml-2 lg:hidden">Star</span>
            </a>
          </li>

          <li class="flex items-center">
            <button
              class="px-4 py-2 mb-3 ml-3 text-xs font-bold uppercase transition-all duration-150 ease-linear bg-white rounded shadow outline-none text-blueGray-700 active:bg-blueGray-50 hover:shadow-md focus:outline-none lg:mr-1 lg:mb-0"
              type="button" onclick="window.location.href='/auth/login' ">
              <i class="fas fa-arrow-alt-circle-down"></i> Sign In
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
import PagesDropdown from "@/components/Dropdowns/PagesDropdown.vue";
export default {
  data() {
    return {
      navbarOpen: false,
    };
  },
  methods: {
    setNavbarOpen: function () {
      this.navbarOpen = !this.navbarOpen;
    },
  },
  components: {
    PagesDropdown,
  },
};
</script>
