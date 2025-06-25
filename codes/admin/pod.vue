<TabView v-else v-model:activeIndex="activeTabIndex" scrollable>
    <TabPanel v-for="(podType, index) in podTypes" :key="podType.id" :header="podType.name" :headerStyle="{ fontWeight: 'bold' }">
        <div class="flex justify-end mb-3">
            <Button label="Tambah Pod" icon="pi pi-plus" class="p-button-sm" @click="openAddPodModal(podType)" />
        </div>
        <!-- display total pod if any -->
        <div v-if="filteredPods(podType.id).length" class="mb-2">Total Pod: {{ filteredPods(podType.id).length }}</div>
        <div v-if="filteredPods(podType.id).length" class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            <div v-for="pod in filteredPods(podType.id)" :key="pod.id" class="border rounded-xl p-4 shadow hover:shadow-md bg-white dark:bg-zinc-800 dark:border-zinc-600">
                <img v-if="pod.pod_type.image" :src="pod.image" class="w-full h-32 object-cover rounded mb-2" />
                <div class="font-bold text-xl">{{ pod.order }}. {{ pod.name }}</div>
                <div class="">Rp{{ pod.pod_type.price.toLocaleString() }}</div>
                <!-- last online unix timestamp to wib -->
                <div class="mt-1">
                    Last Online:
                    {{
                        new Date(pod.last_online * 1000).toLocaleString('id-ID', {
                            timeZone: 'Asia/Jakarta',
                            weekday: 'long', // Senin, Selasa, ...
                            year: 'numeric',
                            month: 'long', // Januari, Februari, ...
                            day: 'numeric',
                            hour: '2-digit',
                            minute: '2-digit',
                            second: '2-digit'
                        })
                    }}
                </div>
                <div class="mt-2">
                    <Button label="Edit" icon="pi pi-pencil" class="p-button-text p-0 text-xs" @click="openEditPodModal(pod)" />
                    <Button label="Hapus" icon="pi pi-trash" class="p-button-text p-0 text-xs text-red-500" @click="deletePod(pod.id, pod.name)" />
                </div>
            </div>
        </div>
        <div v-else class="text-gray-500 dark:text-gray-300 h-[300px] text-center">Belum ada pod untuk tipe ini.</div>
    </TabPanel>
</TabView>