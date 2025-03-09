<template>
  <div class="container h-full px-4 mx-auto">
    <div class="flex items-center content-center justify-center h-full">
      <div class="w-full px-4 lg:w-6/12">
        <div
          class="relative flex flex-col w-full min-w-0 mb-8 break-words border-0 rounded-lg shadow-lg bg-blueGray-200"
        >
          <div class="px-6 py-5 mb-0 rounded-t">
            <div class="mb-3 text-center">
              <h6 class="text-sm font-bold text-blueGray-500">
                Sign in with
              </h6>
            </div>
            <div class="text-center btn-wrapper">
              <button
                class="inline-flex items-center px-4 py-2 mb-1 mr-2 text-xs font-normal font-bold uppercase transition-all duration-150 ease-linear bg-white rounded shadow outline-none active:bg-blueGray-50 text-blueGray-700 focus:outline-none hover:shadow-md"
                type="button"
              >
                <img alt="..." class="w-5 mr-1" :src="github" />
                Github
              </button>
              <button
                class="inline-flex items-center px-4 py-2 mb-1 mr-1 text-xs font-normal font-bold uppercase transition-all duration-150 ease-linear bg-white rounded shadow outline-none active:bg-blueGray-50 text-blueGray-700 focus:outline-none hover:shadow-md"
                type="button"
              >
                <img alt="..." class="w-5 mr-1" :src="google" />
                Google
              </button>
            </div>
            <hr class="mt-6 border-b-1 border-blueGray-300" />
          </div>
          <div class="flex-auto px-4 py-10 pt-0 lg:px-10">
            <div class="mb-3 font-bold text-center text-blueGray-400">
              <small>Or sign in with credentials</small>
            </div>
            <form>
              <div class="relative w-full mb-3">
                <label
                  class="block mb-2 text-xs font-bold uppercase text-blueGray-600"
                  htmlFor="grid-password"
                >
                  Email
                </label>
                <input
                  type="email"
                  class="w-full px-3 py-3 text-sm transition-all duration-150 ease-linear bg-white border-0 rounded shadow placeholder-blueGray-300 text-blueGray-600 focus:outline-none focus:ring"
                  placeholder="Email"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block mb-2 text-xs font-bold uppercase text-blueGray-600"
                  htmlFor="grid-password"
                >
                  Password
                </label>
                <input
                  type="password"
                  class="w-full px-3 py-3 text-sm transition-all duration-150 ease-linear bg-white border-0 rounded shadow placeholder-blueGray-300 text-blueGray-600 focus:outline-none focus:ring"
                  placeholder="Password"
                />
              </div>
              <div>
                <label class="inline-flex items-center cursor-pointer">
                  <input
                    id="customCheckLogin"
                    type="checkbox"
                    class="w-5 h-5 ml-1 transition-all duration-150 ease-linear border-0 rounded form-checkbox text-blueGray-700"
                  />
                  <span class="ml-2 text-sm font-semibold text-blueGray-600">
                    Remember me
                  </span>
                </label>
              </div>

              <div class="mt-6 text-center">
                <button
                  class="w-full px-6 py-3 mb-1 mr-1 text-sm font-bold text-white uppercase transition-all duration-150 ease-linear rounded shadow outline-none bg-blueGray-800 active:bg-blueGray-600 hover:shadow-lg focus:outline-none"
                  type="button"
                >
                  Sign In
                </button>
              </div>
            </form>
          </div>
        </div>
        <div class="relative flex flex-wrap mt-6">
          <div class="w-1/2">
            <a href="javascript:void(0)" class="text-blueGray-200">
              <small>Forgot password?</small>
            </a>
          </div>
          <div class="w-1/2 text-right">
            <router-link to="/auth/register" class="text-blueGray-200">
              <small>Create new account</small>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import github from "@/assets/img/github.svg";
import google from "@/assets/img/google.svg";

export default {
  data() {
    return {
      github,
      google,
    };
  },
};
</script>
