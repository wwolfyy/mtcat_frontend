<template>
  <div class="min-h-screen font-gaegu">
    <header class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-2 sm:px-4 py-4">
        <h1 class="text-4xl sm:text-4xl font-bold text-gray-900 text-center">계양산 고양이들</h1>
        <div class="flex mt-4 border-b border-gray-200">
          <button 
            v-for="tab in tabs" 
            :key="tab.id"
            @click="activeTab = tab.id"
            class="flex-1 py-3 sm:py-2 px-4 text-center text-sm font-semibold sm:text-base rounded-lg transition-all duration-200 ease-in-out"
            :class="{ 
              'bg-gradient-to-r from-yellow-400 to-orange-300 text-black shadow-md transform scale-105 font-bold': activeTab === tab.id,
              'text-gray-600 hover:bg-white hover:shadow-sm': activeTab !== tab.id 
            }"
          >
            {{ tab.name }}
          </button>
        </div>
      </div>
    </header>
    
    <main class="w-screen overflow-x-hidden">
      <MountainViewer v-if="activeTab === 'map'" />
      <ParticipateSection v-else-if="activeTab === 'participate'" />
      <AboutSection v-else-if="activeTab === 'about'" />      
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import MountainViewer from './components/MountainViewer.vue';
import AboutSection from './components/AboutSection.vue';
import ParticipateSection from './components/ParticipateSection.vue';

const tabs = [
  { id: 'map', name: '고양이 지도' }, 
  { id: 'about', name: '소개' },
  { id: 'participate', name: '동참' }
];

const activeTab = ref('map');
</script>
