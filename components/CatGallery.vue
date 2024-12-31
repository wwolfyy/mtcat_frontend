<template>
  <div class="absolute top-full left-0 right-0 bg-white/90 backdrop-blur-sm">
    <!-- Thumbnails section with names -->
    <div class="p-4 flex flex-wrap gap-6 justify-center">
      <div
        v-for="cat in cats"
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

// Log props immediately
console.log('Props received:', props);
console.log('dwelling value:', props.pointId);

defineEmits(['close']);

const cats = ref([]);
const selectedCat = ref(null);

onMounted(async () => {
  const { db } = initializeFirebase();
  const catsCollection = collection(db, 'cats');
  console.log('catsColection:', catsCollection)
  
  console.log('Creating query with dwelling:', props.dwelling);
  
  const catsQuery = query(catsCollection, where('dwelling', '==', props.pointId));
  console.log('Query created:', catsQuery);
  
  try {
    const catsSnapshot = await getDocs(catsQuery);
    console.log('Query snapshot:', catsSnapshot);
    console.log('Number of documents:', catsSnapshot.size);
    
    cats.value = catsSnapshot.docs.map(doc => {
      const data = {
        id: doc.id,
        ...doc.data()
      };
      console.log('Cat document data:', data);
      return data;
    });
  } catch (error) {
    console.error('Error fetching cats:', error);
  }
});
</script>