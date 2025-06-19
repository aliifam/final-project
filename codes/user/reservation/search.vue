<div class="flex flex-col lg:flex-row items-end gap-4">
    <div class="flex-1 w-full">
    <label class="block font-semibold text-white">Lokasi</label>
    <Combobox v-model="selectedBranch">
        <div class="relative w-full">
        <ComboboxButton class="w-full">
            <div
            class="flex items-center p-3 border rounded-lg bg-white/20 backdrop-blur-md"
            >
            <mdi-location class="w-5 h-5 mr-2 text-gray-200" />
            <ComboboxInput
                class="w-full outline-none bg-transparent text-white placeholder-gray-300"
                @change="query = $event.target.value"
                :display-value="(branch) => branch?.name"
                placeholder="Pilih Lokasi"
            />
            </div>
        </ComboboxButton>
        <ComboboxOptions
            class="absolute w-full bg-white/90 rounded-lg mt-1 shadow-lg z-50 text-black"
        >
            <ComboboxOption
            v-for="branch in filteredBranches"
            :key="branch.id"
            :value="branch"
            class="p-2 hover:bg-gray-200 cursor-pointer flex items-center hover:rounded-lg"
            >
            <lucide-hotel class="w-5 h-5 mr-2" />
            {{ branch.name }}
            </ComboboxOption>
        </ComboboxOptions>
        </div>
    </Combobox>
    </div>

    <div class="flex-1 w-full">
    <label class="block font-semibold text-white">Durasi & Tanggal</label>
    <VueDatePicker
        v-model="dateRange"
    />
    </div>
    <div class="w-full md:w-auto">
    <button
        @click="searchRooms"
        class="w-full md:w-fit bg-primary text-white p-3 rounded-lg cursor-pointer font-semibold flex items-center justify-center"
    >
        <mdi-magnify class="w-5 h-5 mr-2" />
        Cari Kamar
    </button>
    </div>
</div>