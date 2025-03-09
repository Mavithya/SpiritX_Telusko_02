<template>
  <div>
    <a
      class="flex items-center px-3 py-2 text-xs font-bold uppercase hover:text-blueGray-500 text-blueGray-700"
      href="#pablo"
      ref="btnDropdownRef"
      v-on:click="toggleDropdown($event)"
    >
      Demo Pages
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
        to="/admin/settings"
        class="block w-full px-4 py-2 text-sm font-normal bg-transparent whitespace-nowrap text-blueGray-700"
      >
        Settings
      </router-link>
      <router-link
        to="/admin/tables"
        class="block w-full px-4 py-2 text-sm font-normal bg-transparent whitespace-nowrap text-blueGray-700"
      >
        Tables
      </router-link>
      <router-link
        to="/admin/maps"
        class="block w-full px-4 py-2 text-sm font-normal bg-transparent whitespace-nowrap text-blueGray-700"
      >
        Maps
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
        No Layout
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
        Profile
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
