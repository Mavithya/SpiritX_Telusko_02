<template>
  <div>
    <navbar />
    <main class="profile-page">
      <section class="relative block h-500-px">
        <div
          class="absolute top-0 w-full h-full bg-center bg-cover"
          style="
            background-image: url('https://img.freepik.com/premium-photo/spectators-expecting-evening-match-green-grass-field-stadium_1199132-32347.jpg');
          "
        >
          <span
            id="blackOverlay"
            class="absolute w-full h-full bg-black opacity-50"
          ></span>
        </div>
        <div
          class="absolute bottom-0 left-0 right-0 top-auto w-full overflow-hidden pointer-events-none h-70-px"
          style="transform: translateZ(0);"
        >
          <svg
            class="absolute bottom-0 overflow-hidden"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="none"
            version="1.1"
            viewBox="0 0 2560 100"
            x="0"
            y="0"
          >
            <polygon
              class="fill-current text-blueGray-200"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>
      </section>
      <section class="relative py-16 bg-blueGray-200">
        <div class="container px-4 mx-auto">
          <div
            class="relative flex flex-col w-full min-w-0 mb-6 -mt-64 break-words bg-white rounded-lg shadow-xl"
          >
            <div class="px-6">
              <div class="flex flex-wrap justify-center">
                <div
                  class="flex justify-center w-full px-4 lg:w-3/12 lg:order-2"
                >
                  <div class="relative">
                    <img
                      alt="..."
                      src="https://img1.hscicdn.com/image/upload/f_auto/lsci/db/PICTURES/CMS/175500/175557.jpg"
                      class="absolute -m-16 -ml-20 align-middle border-none rounded-full shadow-xl lg:-ml-16 max-w-150-px"
                    />
                  </div>
                </div>
                <div
                  class="w-full px-4 lg:w-4/12 lg:order-3 lg:text-right lg:self-center"
                >
                  <div class="px-3 py-6 mt-32 sm:mt-0">
                    <button
                      class="px-4 py-2 mb-1 text-xs font-bold text-white uppercase transition-all duration-150 ease-linear rounded shadow outline-none bg-emerald-500 active:bg-emerald-600 hover:shadow-md focus:outline-none sm:mr-2"
                      type="button"
                    >
                      Add to Team
                    </button>
                  </div>
                </div>
                <div class="w-full px-4 lg:w-4/12 lg:order-1">
                  <div class="flex justify-center py-4 pt-8 lg:pt-4">
                    <div class="p-3 mr-4 text-center">
                      <span
                        class="block text-xl font-bold tracking-wide uppercase text-blueGray-600"
                      >
                        1022
                      </span>
                      <span class="text-sm text-blueGray-400">Friends</span>
                    </div>
                    <div class="p-3 mr-4 text-center">
                      <span
                        class="block text-xl font-bold tracking-wide uppercase text-blueGray-600"
                      >
                        101
                      </span>
                      <span class="text-sm text-blueGray-400">Photos</span>
                    </div>
                    <div class="p-3 text-center lg:mr-4">
                      <span
                        class="block text-xl font-bold tracking-wide uppercase text-blueGray-600"
                      >
                        890
                      </span>
                      <span class="text-sm text-blueGray-400">Comments</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="mt-12 text-center">
                <h3
                  class="mb-2 text-4xl font-semibold leading-normal text-blueGray-700"
                >
                  Dinesh Sandakan
                </h3>
                <div
                  class="mt-0 mb-2 text-sm font-bold leading-normal uppercase text-blueGray-400"
                >
                  <i
                    class="mr-2 text-lg fas fa-map-marker-alt text-blueGray-400"
                  ></i>
                  Ambalangoda, Sri Lanka
                </div>
                <div class="mt-10 mb-2 text-blueGray-600">
                 
                  <i class="mr-2 text-lg fa-solid fa-broom-ball text-blueGray-400"></i>
                  Right Handed Batsman
                </div>
                <div class="mb-2 text-blueGray-600">
                  <i
                    class="mr-2 text-lg fas fa-university text-blueGray-400"
                  ></i>
                  University of Kelaniya
                </div>
              </div>
              <div class="py-10 mt-10 text-left border-t border-blueGray-200 ">
                <div class="flex flex-wrap justify-center">
                  <div class="w-full px-4 lg:w-9/12">
                    <p class="mb-4 text-lg leading-relaxed text-blueGray-700 ">
                      Performance Stat
                    </p>
                    <ul class="mb-4 ">
                      <li>Matches Played: 🔹Tests: 70+ 🔹ODIs: 150+ 🔹 T20Is: 60+</li>
                      <li>Runs Scored :🔹Tests: 5,000+ runs 🔹ODIs: 4,000+ run🔹T20Is: 1,000+ runs</li>
                      <li>Highest Scores :🔹Tests: 164 🔹ODIs: 111🔹T20Is: 66</li>
                    </ul>
                    <a
                      href="javascript:void(0)"
                      class="mt-4 font-normal text-emerald-500"
                    >
                      Show more
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
    <footer-component />
  </div>
</template>
<script>
import Navbar from "@/components/Navbars/AuthNavbar.vue";
import FooterComponent from "@/components/Footers/Footer.vue";

import team2 from "@/assets/img/team-2-800x800.jpg";

export default {
  data() {
    return {
      team2,
    };
  },
  components: {
    Navbar,
    FooterComponent,
  },
};
</script>
