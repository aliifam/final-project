<div class="space-y-4">
    <div>
        <label for="email" class="block text-sm font-medium text-gray-700"
        >Email</label
        >
        <input
        id="email"
        v-model="email"
        type="email"
        placeholder="Enter your email"
        class="w-full p-3 border-2 border-gray-300 rounded-lg focus:outline-none mt-1"
        required
        />
    </div>
    <div>
        <label for="password" class="block text-sm font-medium text-gray-700"
        >Password</label
        >
        <div class="relative">
        <input
            id="password"
            :type="showPassword ? 'text' : 'password'"
            v-model="password"
            placeholder="Enter your password"
            class="w-full p-3 border-2 border-gray-300 rounded-lg focus:outline-none pr-10 mt-1"
            required
        />
        <button
            @click="showPassword = !showPassword"
            class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 hover:text-gray-700 cursor-pointer"
        >
            <material-symbols-visibility
            v-if="!showPassword"
            width="24"
            height="24"
            />
            <material-symbols-visibility-off v-else width="24" height="24" />
        </button>
        </div>
    </div>
    <button
        @click="login"
        class="w-full cursor-pointer bg-primary text-white p-3 rounded-lg hover:bg-primary-dark transition duration-200 flex items-center justify-center font-semibold"
        :disabled="loading"
    >
        <span
        v-if="loading"
        class="animate-spin border-2 border-white border-t-transparent rounded-full w-5 h-5 mr-2"
        ></span>
        {{ loading ? "Logging in..." : "Login" }}
    </button>
    <button
        @click="gotoGoogleLogin"
        class="w-full flex items-center justify-center space-x-2 border border-gray-300 p-3 rounded-lg hover:bg-gray-100 transition duration-200 cursor-pointer"
    >
        <flat-color-icons-google class="w-5 h-5" />
        <span>Login with Google</span>
    </button>
</div>