<template>
  <div>
    <navbar />
    <main>
      <div class="relative flex items-center content-center justify-center pt-16 pb-32 min-h-screen-75">
        <div class="absolute top-0 w-full h-full bg-center bg-cover"
          style="
            background-image: url('https://thumbs.dreamstime.com/b/stadium-cricket-night-bright-color-ai-generated-content-design-background-instagram-facebook-wall-painting-wallpaper-325372484.jpg');">
          <span id="blackOverlay" class="absolute w-full h-full bg-black opacity-50"></span>
        </div>
        <div class="container relative mx-auto">
          <div class="flex flex-wrap items-center">
            <div class="w-full px-4 ml-auto mr-auto text-center lg:w-6/12">
              <div class="pr-12">
                <h1 class="text-5xl font-bold text-white">
                  Build Your Dream Team & Win Big!
                </h1>
                <p class="mt-6 text-xl text-blueGray-200">
                  Join the Inter-University Fantasy Cricket Game and test your skills against the best. Draft players,
                  make strategic moves, and climb the leaderboard!
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="absolute bottom-0 left-0 right-0 top-auto w-full overflow-hidden pointer-events-none h-70-px"
          style="transform: translateZ(0);">
          <svg class="absolute bottom-0 overflow-hidden" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"
            version="1.1" viewBox="0 0 2560 100" x="0" y="0">
            <polygon class="fill-current text-blueGray-200" points="2560 0 2560 100 0 100"></polygon>
          </svg>
        </div>
      </div>

      <section class="pb-20 -mt-24 bg-blueGray-200">
        <div class="container px-4 mx-auto">
          <div class="flex flex-wrap">
            <div class="w-full px-4 pt-6 text-center lg:pt-12 md:w-4/12">
              <div class="relative flex flex-col w-full min-w-0 mb-8 break-words bg-white rounded-lg shadow-lg">
                <div class="flex-auto px-4 py-5">
                  <div
                    class="inline-flex items-center justify-center w-12 h-12 p-3 mb-5 text-center text-white bg-red-400 rounded-full shadow-lg">
                    <i class="fas fa-award"></i>
                  </div>
                  <h6 class="text-xl font-semibold">Awarded Agency</h6>
                  <p class="mt-2 mb-4 text-blueGray-500">
                    Recognized for Excellence in Innovation & Sports, our team behind Cricket11 has been honored for
                    revolutionizing fantasy cricket in the university sports arena.
                  </p>
                </div>
              </div>
            </div>

            <div class="w-full px-4 text-center md:w-4/12">
              <div class="relative flex flex-col w-full min-w-0 mb-8 break-words bg-white rounded-lg shadow-lg">
                <div class="flex-auto px-4 py-5">
                  <div
                    class="inline-flex items-center justify-center w-12 h-12 p-3 mb-5 text-center text-white rounded-full shadow-lg bg-lightBlue-400">
                    <i class="fa-solid fa-bullseye"></i>
                  </div>
                  <h6 class="text-xl font-semibold">Ultimate Fantasy Experience</h6>
                  <p class="mt-2 mb-4 text-blueGray-500">
                    Unleash your cricket strategy with Cricket11! Build your dream team, manage budgets, and compete
                    with fellow cricket fans.
                  </p>
                </div>
              </div>
            </div>

            <div class="w-full px-4 pt-6 text-center md:w-4/12">
              <div class="relative flex flex-col w-full min-w-0 mb-8 break-words bg-white rounded-lg shadow-lg">
                <div class="flex-auto px-4 py-5">
                  <div
                    class="inline-flex items-center justify-center w-12 h-12 p-3 mb-5 text-center text-white rounded-full shadow-lg bg-emerald-400">
                    <i class="fa-solid fa-cloud-bolt"></i>
                  </div>
                  <h6 class="text-xl font-semibold">Real-Time Stats & Insights</h6>
                  <p class="mt-2 mb-4 text-blueGray-500">
                    Stay ahead of the game with instant player updates and real-time performance tracking! Make informed
                    decisions and lead your team to victory!
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div class="flex flex-wrap items-center mt-32">
            <div class="w-full px-4 ml-auto mr-auto md:w-5/12">
              <div
                class="inline-flex items-center justify-center w-16 h-16 p-3 mb-6 text-center bg-white rounded-full shadow-lg text-blueGray-500">
                <i class="text-xl fas fa-user-friends"></i>
              </div>
              <h3 class="mb-2 text-3xl font-semibold leading-normal">
                Why Play Cricket 11?
              </h3>

              <div>
                <ul class="mt-4 mb-4 text-lg font-normal leading-relaxed list-disc list-inside text-blueGray-600">
                  <li>✅ Real University Cricket Players - Pick from the best university cricketers and build your squad.
                  </li>
                  <li>✅ AI-Powered Assistance - Get smart player recommendations with Spiriter Chatbot.</li>
                  <li>✅ Leaderboard Competition - Battle with friends and fellow cricket fans.</li>
                  <li>✅ Budget Management - Use your Rs.9,000,000 wisely to create the perfect team.</li>
                  <li>✅ Live Player Stats & Updates - Stay updated with real-time performance data.</li>
                </ul>
              </div>


              <router-link to="/admin" class="mt-8 text-2xl font-bold text-blueGray-700 ">
                Check Players!
              </router-link>
            </div>

            <div class="w-full px-4 ml-auto mr-auto md:w-4/12">
              <div
                class="relative flex flex-col w-full min-w-0 mb-6 break-words bg-white rounded-lg shadow-lg bg-emerald-500">
                <img alt="..." src="https://img.freepik.com/premium-photo/cricket-player_841014-12028.jpg?w=2000"
                  class="align-middle rounded-t-lg size-40" />
                <blockquote class="relative p-8 mb-4">
                  <svg preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 583 95"
                    class="absolute left-0 block w-full h-95-px -top-94-px">
                    <polygon points="-30,95 583,95 583,65" class="fill-current text-emerald-500"></polygon>
                  </svg>
                  <h4 class="text-xl font-bold text-white">
                    Start Playing Today!
                  </h4>
                  <p class="mt-2 font-normal text-white text-md">🔹 Step 1: Create your account</p>
                  <p class="mt-2 font-normal text-white text-md">🔹 Step 2: Pick your best 11</p>
                  <p class="mt-2 font-normal text-white text-md">🔹 Step 3: Manage & compete</p>
                </blockquote>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="relative py-20">
        <div class="absolute top-0 left-0 right-0 bottom-auto w-full h-20 -mt-20 overflow-hidden pointer-events-none"
          style="transform: translateZ(0);">
          <svg class="absolute bottom-0 overflow-hidden" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"
            version="1.1" viewBox="0 0 2560 100" x="0" y="0">
            <polygon class="text-white fill-current" points="2560 0 2560 100 0 100"></polygon>
          </svg>
        </div>

        <div class="container px-4 mx-auto">
          <div class="flex flex-wrap items-center">
            <div class="w-full px-4 ml-auto mr-auto md:w-4/12">
              <img alt="..." class="h-auto max-w-full align-middle border-none rounded-lg shadow-xl"
                src="https://c4.wallpaperflare.com/wallpaper/412/331/580/sports-cricket-wallpaper-preview.jpg" />
            </div>
            <div class="w-full px-4 ml-auto mr-auto md:w-5/12">
              <div class="md:pr-12">
                <div
                  class="inline-flex items-center justify-center w-16 h-16 p-3 mb-6 text-center rounded-full shadow-lg text-emerald-600 bg-emerald-300">
                  <i class="text-xl fas fa-rocket"></i>
                </div>
                <h3 class="text-3xl font-semibold">How It Works? 🏆</h3>
                <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
                  Think you have what it takes to win? Join now and become the Cricket 11 Champion!
                </p>
                <ul class="mt-6 list-none">
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="inline-block px-2 py-2 mr-4 font-semibold uppercase rounded-full text-normal text-emerald-600 bg-emerald-200">
                          <i class="fa-solid fa-user-plus"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-600">
                          Sign Up & Log In - Create your account and start playing.
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="inline-block px-3 py-2 mr-3 font-semibold uppercase rounded-full text-normal text-emerald-600 bg-emerald-200">
                          <i class="fa-solid fa-circle-check"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-600">
                          Select Your Team - Pick 11 players within your budget
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="inline-block px-2 py-2 mr-4 font-semibold uppercase rounded-full text-normal text-emerald-600 bg-emerald-200">
                          <i class="fa-solid fa-people-roof"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-600">
                          Manage Your Squad - Swap players, track performance, and optimize your team.
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="inline-block px-2 py-2 mr-4 font-semibold uppercase rounded-full text-normal text-emerald-600 bg-emerald-200">
                          <i class="fa-solid fa-ranking-star"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-600">
                          Compete on the Leaderboard - Earn points based on real match performances!
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="inline-block px-2 py-2 mr-4 font-semibold uppercase rounded-full text-normal text-emerald-600 bg-emerald-200">
                          <i class="fa-solid fa-headset"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-600">
                          Get AI Assistance - Our chatbot Spiriter helps you make better choices! </h4>
                      </div>
                    </div>
                  </li>

                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="pt-20 pb-48">
        <div class="container px-4 mx-auto">
          <div class="flex flex-wrap justify-center mb-24 text-center">
            <div class="w-full px-4 lg:w-6/12">
              <h2 class="text-4xl font-semibold">Here are our heroes</h2>
              <p class="m-4 text-lg leading-relaxed text-blueGray-500">
                At Cricket 11, we celebrate the passion, dedication, and strategic brilliance of our top fantasy cricket
                players. These champions have mastered the art of team selection, making bold predictions, and leading
                their squads to glory.
              </p>
            </div>
          </div>
          <div class="flex flex-wrap">
            <div class="w-full px-4 mb-12 md:w-6/12 lg:w-3/12 lg:mb-0">
              <div class="px-6">
                <img alt="..." :src="team1" class="mx-auto rounded-full shadow-lg max-w-120-px" />
                <div class="pt-6 text-center">
                  <h5 class="text-xl font-bold">Tharindu Gamage</h5>
                  <p class="mt-2 text-sm font-semibold uppercase text-blueGray-400">
                    "King of Captaincy"
                  </p>
                  <p class="mt-4 text-blueGray-700">🏆 Top Scorer | 5x League Winner</p>
                  <div class="mt-6">
                    <button
                      class="w-16 h-8 mb-1 mr-1 text-white rounded-full outline-none bg-lightBlue-400 focus:outline-none"
                      type="button">
                      <i class="fa-solid fa-eye"></i>
                    </button>

                  </div>
                </div>
              </div>
            </div>
            <div class="w-full px-4 mb-12 md:w-6/12 lg:w-3/12 lg:mb-0">
              <div class="px-6">
                <img alt="..." :src="team2" class="mx-auto rounded-full shadow-lg max-w-120-px" />
                <div class="pt-6 text-center">
                  <h5 class="text-xl font-bold">Suranga Bandara</h5>
                  <p class="mt-2 text-sm font-semibold uppercase text-blueGray-400">
                    "The Game Changer"
                  </p>
                  <p class="mt-4 text-blueGray-700">🏆 Consistently in Top 10 Expert in Bowling Picks</p>
                  <div class="mt-6">
                    <button
                      class="w-16 h-8 mb-1 mr-1 text-white rounded-full outline-none bg-lightBlue-400 focus:outline-none"
                      type="button">
                      <i class="fa-solid fa-eye"></i>
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="w-full px-4 mb-12 md:w-6/12 lg:w-3/12 lg:mb-0">
              <div class="px-6">
                <img alt="..." :src="team3" class="mx-auto rounded-full shadow-lg max-w-120-px" />
                <div class="pt-6 text-center">
                  <h5 class="text-xl font-bold">Bhanuka Rajapaksa</h5>
                  <p class="mt-2 text-sm font-semibold uppercase text-blueGray-400">
                    "Tactical Genius"
                  </p>
                  <p class="mt-4 text-blueGray-700">🏆 Highest Winning Streak Pro at All-Rounders</p>
                  <div class="mt-6">
                    <button
                      class="w-16 h-8 mb-1 mr-1 text-white rounded-full outline-none bg-lightBlue-400 focus:outline-none"
                      type="button">
                      <i class="fa-solid fa-eye"></i>
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="w-full px-4 mb-12 md:w-6/12 lg:w-3/12 lg:mb-0">
              <div class="px-6">
                <img alt="..." :src="team4" class="mx-auto rounded-full shadow-lg max-w-120-px" />
                <div class="pt-6 text-center">
                  <h5 class="text-xl font-bold">Sandakan Hasaranga</h5>
                  <p class="mt-2 text-sm font-semibold uppercase text-blueGray-400">
                    "The Risk Taker"
                  </p>
                  <p class="mt-4 text-blueGray-700">🏆 3x Weekly Winner | Best at Uncapped Player Picks</p>
                  <div class="mt-6">
                    <button
                      class="w-16 h-8 mb-1 mr-1 text-white rounded-full outline-none bg-lightBlue-400 focus:outline-none"
                      type="button">
                      <i class="fa-solid fa-eye"></i>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="relative block pb-20 bg-blueGray-800">
        <div class="absolute top-0 left-0 right-0 bottom-auto w-full h-20 -mt-20 overflow-hidden pointer-events-none"
          style="transform: translateZ(0);">
          <svg class="absolute bottom-0 overflow-hidden" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"
            version="1.1" viewBox="0 0 2560 100" x="0" y="0">
            <polygon class="fill-current text-blueGray-800" points="2560 0 2560 100 0 100"></polygon>
          </svg>
        </div>

        <div class="container px-4 mx-auto lg:pt-24 lg:pb-64">
          <div class="flex flex-wrap justify-center text-center">
            <div class="w-full px-4 lg:w-6/12">
              <h2 class="text-4xl font-semibold text-white">
                Join the Game, Make Your Mark
              </h2>
              <p class="mt-4 mb-4 text-2xl leading-relaxed text-blueGray-400">
                Your Fantasy, Your Victory!
              </p>
            </div>
          </div>
          <div class="flex flex-wrap justify-center mt-12">
            <div class="w-full px-4 text-center lg:w-3/12">
              <div
                class="inline-flex items-center justify-center w-12 h-12 p-3 bg-white rounded-full shadow-lg text-blueGray-800">
                <i class="text-xl fas fa-medal"></i>
              </div>
              <h6 class="mt-5 text-xl font-semibold text-white">
                Excelent Services
              </h6>
              <p class="mt-2 mb-4 text-blueGray-400">
                We deliver a seamless, fair, and exciting fantasy cricket experience  built for performance and rewards!
              </p>
            </div>
            <div class="w-full px-4 text-center lg:w-3/12">
              <div
                class="inline-flex items-center justify-center w-12 h-12 p-3 bg-white rounded-full shadow-lg text-blueGray-800">
                <i class="text-xl fas fa-poll"></i>
              </div>
              <h5 class="mt-5 text-xl font-semibold text-white">
                Grow your market
              </h5>
              <p class="mt-2 mb-4 text-blueGray-400">
                Expand your reach and engage more cricket fans with our dynamic platform
              </p>
            </div>
            <div class="w-full px-4 text-center lg:w-3/12">
              <div
                class="inline-flex items-center justify-center w-12 h-12 p-3 bg-white rounded-full shadow-lg text-blueGray-800">
                <i class="text-xl fas fa-lightbulb"></i>
              </div>
              <h5 class="mt-5 text-xl font-semibold text-white">
                Ultimate Fair Play
              </h5>
              <p class="mt-2 mb-4 text-blueGray-400">
                We ensure fairness, offering equal opportunities for success, with systems that prevent cheating and foster healthy competition.
</p>
            </div>
          </div>
        </div>
      </section>
      <section class="relative block py-24 lg:pt-0 bg-blueGray-800">
        <div class="container px-4 mx-auto">
          <div class="flex flex-wrap justify-center -mt-48 lg:-mt-64">
            <div class="w-full px-4 lg:w-6/12">
              <div class="relative flex flex-col w-full min-w-0 mb-6 break-words rounded-lg shadow-lg bg-blueGray-200">
                <div class="flex-auto p-5 lg:p-10">
                  <h4 class="text-2xl font-semibold">
                    Want any help from us?
                  </h4>
                  <p class="mt-1 mb-4 leading-relaxed text-blueGray-500">
                    Complete this form and we will get back to you in 24 hours.
                  </p>
                  <div class="relative w-full mt-8 mb-3">
                    <label class="block mb-2 text-xs font-bold uppercase text-blueGray-600" htmlFor="full-name">
                      Full Name
                    </label>
                    <input type="text"
                      class="w-full px-3 py-3 text-sm transition-all duration-150 ease-linear bg-white border-0 rounded shadow placeholder-blueGray-300 text-blueGray-600 focus:outline-none focus:ring"
                      placeholder="Full Name" />
                  </div>

                  <div class="relative w-full mb-3">
                    <label class="block mb-2 text-xs font-bold uppercase text-blueGray-600" htmlFor="email">
                      Email
                    </label>
                    <input type="email"
                      class="w-full px-3 py-3 text-sm transition-all duration-150 ease-linear bg-white border-0 rounded shadow placeholder-blueGray-300 text-blueGray-600 focus:outline-none focus:ring"
                      placeholder="Email" />
                  </div>

                  <div class="relative w-full mb-3">
                    <label class="block mb-2 text-xs font-bold uppercase text-blueGray-600" htmlFor="message">
                      Message
                    </label>
                    <textarea rows="4" cols="80"
                      class="w-full px-3 py-3 text-sm bg-white border-0 rounded shadow placeholder-blueGray-300 text-blueGray-600 focus:outline-none focus:ring"
                      placeholder="Type a message..." />
                  </div>
                  <div class="mt-6 text-center">
                    <button
                      class="px-6 py-3 mb-1 mr-1 text-sm font-bold text-white uppercase transition-all duration-150 ease-linear rounded shadow outline-none bg-blueGray-800 active:bg-blueGray-600 hover:shadow-lg focus:outline-none"
                      type="button">
                      Send Message
                    </button>
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

import team1 from "@/assets/img/team-1-800x800.jpg";
import team2 from "@/assets/img/team-2-800x800.jpg";
import team3 from "@/assets/img/team-3-800x800.jpg";
import team4 from "@/assets/img/team-4-800x800.jpg";

export default {
  data() {
    return {
      team1,
      team2,
      team3,
      team4,
    };
  },
  components: {
    Navbar,
    FooterComponent,
  },
};
</script>
