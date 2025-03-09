<template>
  <nav
    class="fixed top-0 z-50 flex flex-wrap items-center justify-between w-full px-2 py-3 bg-white shadow navbar-expand-lg"
  >
    <div
      class="container flex flex-wrap items-center justify-between px-4 mx-auto"
    >
      <div
        class="relative flex justify-between w-full lg:w-auto lg:static lg:block lg:justify-start"
      >
        <router-link to="/">
          <a
            class="inline-block py-2 mr-4 text-sm font-bold leading-relaxed uppercase text-blueGray-700 whitespace-nowrap"
            href="#pablo"
          >
            Cricket 11
          </a>
        </router-link>
        <button
          class="block px-3 py-1 text-xl leading-none bg-transparent border border-transparent border-solid rounded outline-none cursor-pointer lg:hidden focus:outline-none"
          type="button"
          v-on:click="setNavbarOpen"
        >
          <i class="fas fa-bars"></i>
        </button>
      </div>
      <div
        class="items-center flex-grow lg:flex"
        :class="[navbarOpen ? 'block' : 'hidden']"
        id="example-navbar-warning"
      >
        <ul class="flex flex-col mr-auto list-none lg:flex-row">
          <li class="flex items-center">
            <a
              class="flex items-center px-3 py-2 text-xs font-bold uppercase hover:text-blueGray-500 text-blueGray-700"
              href="https://www.creative-tim.com/learning-lab/tailwind/vue/overview/notus?ref=vn-index-navbar"
            >
              <i
                class="mr-2 text-lg text-blueGray-400 far fa-file-alt leading-lg"
              />
              Docs
            </a>
          </li>
        </ul>
        <ul class="flex flex-col list-none lg:flex-row lg:ml-auto">
          <li class="flex items-center">
            <index-dropdown />
          </li>
          <li class="flex items-center">
            <a
              class="flex items-center px-3 py-2 text-xs font-bold uppercase hover:text-blueGray-500 text-blueGray-700"
              href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdemos.creative-tim.com%2Fvue-notus%2F%23%2F"
              target="_blank"
            >
              <i class="text-lg text-blueGray-400 fab fa-facebook leading-lg" />
              <span class="inline-block ml-2 lg:hidden">Share</span>
            </a>
          </li>

          <li class="flex items-center">
            <a
              class="flex items-center px-3 py-2 text-xs font-bold uppercase hover:text-blueGray-500 text-blueGray-700"
              href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fdemos.creative-tim.com%2Fvue-notus%2F%23%2F&text=Start%20your%20development%20with%20a%20Free%20Tailwind%20CSS%20and%20VueJS%20UI%20Kit%20and%20Admin.%20Let%20Vue%20Notus%20amaze%20you%20with%20its%20cool%20features%20and%20build%20tools%20and%20get%20your%20project%20to%20a%20whole%20new%20level.%20"
              target="_blank"
            >
              <i class="text-lg text-blueGray-400 fab fa-twitter leading-lg" />
              <span class="inline-block ml-2 lg:hidden">Tweet</span>
            </a>
          </li>

          <li class="flex items-center">
            <a
              class="flex items-center px-3 py-2 text-xs font-bold uppercase hover:text-blueGray-500 text-blueGray-700"
              href="https://github.com/creativetimofficial/vue-notus?ref=vn-index-navbar"
              target="_blank"
            >
              <i class="text-lg text-blueGray-400 fab fa-github leading-lg" />
              <span class="inline-block ml-2 lg:hidden">Star</span>
            </a>
          </li>

          <li class="flex items-center">
            <button
              class="px-4 py-2 mb-3 ml-3 text-xs font-bold text-white uppercase transition-all duration-150 ease-linear rounded shadow outline-none bg-emerald-500 active:bg-emerald-600 hover:shadow-lg focus:outline-none lg:mr-1 lg:mb-0"
              type="button"
            >
              <i class="fas fa-arrow-alt-circle-down"></i> Download
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import IndexDropdown from "@/components/Dropdowns/IndexDropdown.vue";

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
    IndexDropdown,
  },
};
</script>
