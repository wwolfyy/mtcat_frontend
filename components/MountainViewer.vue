`<template>
  <div class="relative w-full">
    <div class="w-full aspect-[16/9] relative">
      <img 
        :src="mountainImage" 
        alt="Satellite view of mountain"
        class="absolute inset-0 w-full h-full object-contain"
      />
      <div 
        v-for="point in points" 
        :key="point.id"
        :style="{ left: point.x + '%', top: point.y + '%' }"
        class="absolute -translate-x-1/2 -translate-y-1/2"
        @mouseover="handleMouseOver(point)"
        @mouseleave="handleMouseLeave"
        @click="handlePointClick(point)"
      >        
        <div 
          v-show="activePoint?.id !== point.id"
          class="w-8 h-8 bg-null rounded-full cursor-pointer ring-4 ring-white"
        ></div>
        <div 
          class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 text-black font-semibold text-sm 
          whitespace-nowrap bg-yellow-400 rounded-full px-2 py-1"          
        >
          {{ point.title }}
        </div>     
        <div 
          v-if="activePoint?.id === point.id"
          class="absolute w-32 h-32 -translate-x-1/2 -translate-y-1/2 border-2 border-white rounded-full"
          :style="{ left: '50%', top: '50%' }"
        ></div>
      </div>
      
      <CatGallery_ 
        v-if="selectedPoint"
        :point-id="selectedPoint.id"
        @close="selectedPoint = null"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { collection, getDocs } from 'firebase/firestore';
import { initializeFirebase } from '~/utils/firebase';
import CatGallery_ from './CatGallery_.vue';

const mountainImage = ref('/images/screenshot_mt_geyang_50.png');
const points = ref([]);
const activePoint = ref(null);
const selectedPoint = ref(null);

// New methods to handle events
const handleMouseOver = (point) => {
  activePoint.value = point;
  console.log('Hover - Active Point:', point);
  console.log('All properties:', JSON.stringify(point, null, 2));
};

const handleMouseLeave = () => {
  console.log('Mouse Leave - Previous Active Point:', activePoint.value);
  activePoint.value = null;
};

const handlePointClick = (point) => {
  selectedPoint.value = point;
  console.log('Click - Selected Point:', point);
  console.log('All properties:', JSON.stringify(point, null, 2));
};

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