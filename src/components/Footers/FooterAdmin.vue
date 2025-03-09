<template>
  <footer class="block py-4">
    <div class="container px-4 mx-auto">
      <hr class="mb-4 border-b-1 border-blueGray-200" />
      <div
        class="flex flex-wrap items-center justify-center md:justify-between"
      >
        <div class="w-full px-4 md:w-4/12">
          <div
            class="py-1 text-sm font-semibold text-center text-blueGray-500 md:text-left"
          >
            Copyright © {{ date }}
            <a
              href=""
              class="py-1 text-sm font-semibold text-blueGray-500 hover:text-blueGray-700"
            >
              Creative Tim
            </a>
          </div>
        </div>
        <div class="w-full px-4 md:w-8/12">
          <ul class="flex flex-wrap justify-center list-none md:justify-end">
            <li>
              <a
                href=""
                class="block px-3 py-1 text-sm font-semibold text-blueGray-600 hover:text-blueGray-800"
              >
                Creative Tim
              </a>
            </li>
            <li>
              <a
                href=""
                class="block px-3 py-1 text-sm font-semibold text-blueGray-600 hover:text-blueGray-800"
              >
                About Us
              </a>
            </li>
            <li>
              <a
                href=""
                class="block px-3 py-1 text-sm font-semibold text-blueGray-600 hover:text-blueGray-800"
              >
                Blog
              </a>
            </li>
            <li>
              <a
                href=""
                class="block px-3 py-1 text-sm font-semibold text-blueGray-600 hover:text-blueGray-800"
              >
                MIT License
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      date: new Date().getFullYear(),
    };
  },
};
</script>
