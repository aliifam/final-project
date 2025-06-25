<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
    <Card v-for="ota in otas" :key="ota.id" class="shadow-md border">
        <template #title>
            <div class="flex items-center justify-between">
                <span>{{ ota.name }}</span>
                <Button v-if="ota.guide" icon="pi pi-file-pdf" class="p-button-text p-button-sm" @click="downloadGuide(ota.guide)" title="Lihat Panduan" />
            </div>
        </template>

        <template #content>
            <img :src="ota.image" alt="OTA Logo" class="w-full h-28 bg-white p-2 rounded-lg object-contain mb-2" />
            <div class="text-sm mb-2">
                Status:
                <span :class="['px-3 py-1 rounded-full text-sm font-semibold', isActive(ota.id) ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800']">
                    {{ isActive(ota.id) ? 'Aktif' : 'Nonaktif' }}
                </span>
            </div>
            <Button
                :label="isActive(ota.id) ? 'Nonaktifkan' : 'Aktifkan'"
                :icon="isActive(ota.id) ? 'pi pi-times' : 'pi pi-check'"
                :class="isActive(ota.id) ? 'p-button-danger' : 'p-button-primary'"
                @click="isActive(ota.id) ? deactivateOta(ota.id) : activateOta(ota.id)"
                class="w-full"
            />
        </template>
    </Card>
</div>