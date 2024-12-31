<template>
  <div class="min-h-screen">
    <header class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-2 sm:px-4 py-4">
        <h1 class="text-xl sm:text-2xl font-bold text-gray-900">계양산 고양이들</h1>
        <div class="flex mt-4 border-b border-gray-200">
          <button 
            v-for="tab in tabs" 
            :key="tab.id"
            @click="activeTab = tab.id"
            class="flex-1 py-3 sm:py-2 px-2 sm:px-4 text-center text-sm sm:text-base text-gray-700 hover:text-gray-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
            :class="{ 'border-b-2 border-black font-bold': activeTab === tab.id }"
          >
            {{ tab.name }}
          </button>
        </div>
      </div>
    </header>
    
    <main class="w-screen overflow-x-hidden">
      <MountainViewer v-if="activeTab === 'map'" />
      <div v-else-if="activeTab === 'participate'" class="max-w-7xl mx-auto px-4 py-4">
        동참 페이지
      </div>
      <div v-else-if="activeTab === 'about'" class="max-w-7xl mx-auto px-4 py-4">
        소개 페이지
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import MountainViewer_ from './components/MountainViewer_.vue';

const tabs = [
  { id: 'map', name: '고양이 지도' },
  { id: 'participate', name: '소개' },
  { id: 'about', name: '동참' }
];

const activeTab = ref('map');
</script>