<template>
    <!-- <div class="absolute top-full left-0 right-0 bg-white/90 backdrop-blur-sm"> -->
    <div class="fixed inset-0 bg-white/90 backdrop-blur-sm overflow-y-auto">
      <!-- Current Inhabitants -->
      <h2 class="text-lg font-semibold text-gray-700 p-4 text-center mt-12">지금 살고 있는 냥이들</h2>
      <div class="p-4 flex flex-wrap gap-6 justify-center">
        <div
          v-for="cat in currentCats"
          :key="cat.id"
          class="flex flex-col items-center"
        >
          <button
            @click="selectedCat = cat"
            class="relative w-16 h-16 rounded-full overflow-hidden transition-transform hover:scale-110 mb-2"
            :class="{ 'ring-4 ring-red-500': selectedCat?.id === cat.id }"
          >
            <img
              :src="cat.thumbnailUrl"
              :alt="cat.name"
              class="w-full h-full object-cover"
            />
          </button>
          <span class="text-sm font-medium text-gray-700">{{ cat.name }}</span>
        </div>
      </div>
  
      <!-- Previous Inhabitants -->
      <h2 class="text-lg font-semibold text-gray-700 p-4 text-center">이전에 살던 냥이들</h2>
      <div class="p-4 flex flex-wrap gap-6 justify-center">
        <div
          v-for="cat in prevCats"
          :key="cat.id"
          class="flex flex-col items-center"
        >
          <button
            @click="selectedCat = cat"
            class="relative w-16 h-16 rounded-full overflow-hidden transition-transform hover:scale-110 mb-2"
            :class="{ 'ring-4 ring-red-500': selectedCat?.id === cat.id }"
          >
            <img
              :src="cat.thumbnailUrl"
              :alt="cat.name"
              class="w-full h-full object-cover"
            />
          </button>
          <span class="text-sm font-medium text-gray-700">{{ cat.name }}</span>
        </div>
      </div>
  
    <!-- CatInfo overlay -->
    <div 
      v-if="selectedCat"
      class="fixed inset-x-0 top-0 max-h-[80vh] overflow-y-auto bg-white/90 backdrop-blur-sm"
    >
      <CatInfo
        :cat="selectedCat"
      />
      <div class="p-4 border-t border-gray-200">
        <button 
          @click="selectedCat = null"
          class="px-4 py-2 bg-gray-800 text-white rounded-lg w-full"
        >
          Back to Thumbnails
        </button>
      </div>
    </div>

    <!-- Main close button -->
    <div class="p-4 border-t border-gray-200">
      <button 
        @click="$emit('close')"
        class="px-4 py-2 bg-gray-800 text-white rounded-lg w-full"
      >
        Close
      </button>
    </div>
    </div>
  </template>
  
  <script setup>
    import { ref, onMounted } from 'vue';
    import { collection, query, where, getDocs } from 'firebase/firestore';
    import { initializeFirebase } from '~/utils/firebase';
    import CatInfo from './CatInfo.vue';
  
  const props = defineProps({
    pointId: {
      type: String,
      required: true
    }
  });
  
  defineEmits(['close']);
  
  const currentCats = ref([]);
  const prevCats = ref([]);
  const selectedCat = ref(null);
  
  onMounted(async () => {
    const { db } = initializeFirebase();
    const catsCollection = collection(db, 'cats');
    
    // Query current inhabitants
    const currentQuery = query(catsCollection, where('dwelling', '==', props.pointId));
    const currentSnapshot = await getDocs(currentQuery);
    currentCats.value = currentSnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
  
    // Query previous inhabitants
    const prevQuery = query(catsCollection, where('prev_dwelling', '==', props.pointId));
    const prevSnapshot = await getDocs(prevQuery);
    prevCats.value = prevSnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
  });
  </script>