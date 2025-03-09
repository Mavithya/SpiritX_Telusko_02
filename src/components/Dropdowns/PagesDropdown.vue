<template>
  <div>
    <a
      class="flex items-center px-3 py-4 text-xs font-bold uppercase lg:text-white lg:hover:text-blueGray-200 text-blueGray-700 lg:py-2"
      href="#pablo"
      ref="btnDropdownRef"
      v-on:click="toggleDropdown($event)"
    >
      <i class="text-lg fas fa-bars leading-lg text-blueGray-400" />
    </a>
    <div
      ref="popoverDropdownRef"
      class="z-50 float-left py-2 text-base text-left list-none bg-white rounded shadow-lg min-w-48"
      v-bind:class="{
        hidden: !dropdownPopoverShow,
        block: dropdownPopoverShow,
      }"
    >
      <span
        class="block w-full px-4 pt-2 pb-0 text-sm font-bold bg-transparent whitespace-nowrap text-blueGray-400"
      >
        Admin Layout
      </span>
      <router-link
        to="/admin/dashboard"
        class="block w-full px-4 py-2 text-sm font-normal bg-transparent whitespace-nowrap text-blueGray-700"
      >
        Dashboard
      </router-link>
      
      <router-link
        to="/admin/tables"
        class="block w-full px-4 py-2 text-sm font-normal bg-transparent whitespace-nowrap text-blueGray-700"
      >
        Your Team
      </router-link>
     
      <div class="h-0 mx-4 my-2 border border-solid border-blueGray-100" />
      <span
        class="block w-full px-4 pt-2 pb-0 text-sm font-bold bg-transparent whitespace-nowrap text-blueGray-400"
      >
        Auth Layout
      </span>
      <router-link
        to="/auth/login"
        class="block w-full px-4 py-2 text-sm font-normal bg-transparent whitespace-nowrap text-blueGray-700"
      >
        Login
      </router-link>
      <router-link
        to="/auth/register"
        class="block w-full px-4 py-2 text-sm font-normal bg-transparent whitespace-nowrap text-blueGray-700"
      >
        Register
      </router-link>
      <div class="h-0 mx-4 my-2 border border-solid border-blueGray-100" />
      <span
        class="block w-full px-4 pt-2 pb-0 text-sm font-bold bg-transparent whitespace-nowrap text-blueGray-400"
      >
        Main Layout
      </span>
      <router-link
        to="/landing"
        class="block w-full px-4 py-2 text-sm font-normal bg-transparent whitespace-nowrap text-blueGray-700"
      >
        Landing
      </router-link>
      <router-link
        to="/profile"
        class="block w-full px-4 py-2 text-sm font-normal bg-transparent whitespace-nowrap text-blueGray-700"
      >
       Player Profile
      </router-link>
    </div>
  </div>
</template>
<script>
import { createPopper } from "@popperjs/core";

export default {
  data() {
    return {
      dropdownPopoverShow: false,
    };
  },
  methods: {
    toggleDropdown: function (event) {
      event.preventDefault();
      if (this.dropdownPopoverShow) {
        this.dropdownPopoverShow = false;
      } else {
        this.dropdownPopoverShow = true;
        createPopper(this.$refs.btnDropdownRef, this.$refs.popoverDropdownRef, {
          placement: "bottom-start",
        });
      }
    },
  },
};
</script>
