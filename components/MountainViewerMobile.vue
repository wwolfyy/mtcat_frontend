<template>
  <div class="relative w-full">
    <div class="w-full aspect-[16/9] relative">
      <img
        :src="mountainImage"
        alt="Satellite view of mountain"
        class="absolute inset-0 w-full h-full object-contain"
      />
      <div
        v-for="(point, index) in orderedPoints"
        :key="point.id"
        :style="{ left: point.x + '%', top: point.y + '%' }"
        class="absolute -translate-x-1/2 -translate-y-1/2"
        @click="handlePointClick(point)"
        @mouseover="handleMouseOver(point)"
        @mouseleave="handleMouseLeave"
      >
        <div
          class="w-8 h-8 bg-yellow-400 rounded-full flex items-center justify-center text-black font-bold"
          :class="{ 'ring-4': activePoint?.id === point.id }"
        >
          {{ index + 1 }}
        </div>
      </div>
    </div>
    <table class="w-full mt-4 border-collapse modern-table">
      <thead>
        <tr>
          <th class="border p-2">#</th>
          <th class="border p-2">Title</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(point, index) in orderedPoints"
          :key="point.id"
          @click="handleRowClick(point)"
          class="cursor-pointer hover:bg-gray-200"
        >
          <td class="border p-2 text-center">{{ index + 1 }}</td>
          <td class="border p-2">{{ point.title }}</td>
        </tr>
      </tbody>
    </table>
    <CatGallery
      v-if="selectedPoint"
      :point-id="selectedPoint.id"
      @close="selectedPoint = null"
      class="fixed inset-0 z-50"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { collection, getDocs } from 'firebase/firestore';
import { initializeFirebase } from '~/utils/firebase';
import CatGallery from './CatGallery.vue';

const mountainImage = ref('/images/screenshot_mt_geyang_50.png');
const points = ref([]);
const activePoint = ref(null);
const selectedPoint = ref(null);

const handleMouseOver = (point) => {
  activePoint.value = point;
};

const handleMouseLeave = () => {
  activePoint.value = null;
};

const handlePointClick = (point) => {
  selectedPoint.value = point;
};

const handleRowClick = (point) => {
  selectedPoint.value = point;
};

const orderedPoints = computed(() => {
  return points.value.slice().sort((a, b) => a.x - b.x);
});

onMounted(async () => {
  const { db } = initializeFirebase();
  const pointsCollection = collection(db, 'points');
  const pointsSnapshot = await getDocs(pointsCollection);

  points.value = pointsSnapshot.docs.map(doc => ({
    id: doc.id,
    ...doc.data()
  }));
});
</script>

<style scoped>
.modern-table {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.modern-table th, .modern-table td {
  padding: 12px 15px;
  text-align: left;
}

.modern-table th {
  background-color: #f4f4f4;
  font-weight: bold;
}

.modern-table tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.modern-table tbody tr:hover {
  background-color: #f1f1f1;
}
</style>