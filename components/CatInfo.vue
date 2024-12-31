<template>
  <div class="p-4">
    <div class="flex justify-center mb-4">
      <img 
        :src="cat.thumbnailUrl" 
        :alt="cat.name"
        class="w-32 h-32 rounded-full object-cover"
      />
    </div>    
    <div class="space-y-4">
      <h3 class="text-xl font-bold bg-white/80 py-2">{{ cat.name }}</h3>
      
      <div class="mt-4">
        <h4 class="font-semibold text-gray-700"></h4>
        <p class="mt-2 text-gray-600">{{ cat.description }}</p>
      </div> 
      <div class="flex items-center">
        <span class="w-24 font-semibold text-gray-700">출생연도:</span>
        <span class="text-gray-600">{{ cat.date_of_birth }}</span>
      </div>         
      <div class="flex items-center">
        <span class="w-24 font-semibold text-gray-700">성별:</span>
        <span class="text-gray-600">{{ cat.sex }}</span>
      </div>          

      <div class="flex items-center">
        <span class="w-24 font-semibold text-gray-700">거주지:</span>
        <span class="text-gray-600">{{ cat.dwelling }}</span>
      </div>          

      <div class="flex items-center">
        <span class="w-24 font-semibold text-gray-700">현상태:</span>
        <span class="text-gray-600">{{ getStatusEmoji(cat.status) }} {{ cat.status }}</span>
      </div>   
      <div class="mt-4">
        <h4 class="font-semibold text-gray-700">성격:</h4>
        <p class="text-gray-600">{{ cat.character }}</p>
      </div>        
      <div class="flex items-center">
        <span class="w-24 font-semibold text-gray-700">엄마:</span>
        <span class="text-gray-600">{{ cat.parents }}</span>
      </div>
      <div class="flex items-center">
        <span class="w-24 font-semibold text-gray-700">애:</span>
        <span class="text-gray-600">{{ cat.offspring }}</span>
      </div>    
      <div class="mt-4">
        <h4 class="font-semibold text-gray-700">건강상태:</h4>
        <p class="text-gray-600">{{ cat.sickness || 'Unknown' }}</p>
      </div>
      <div class="flex items-center">
        <span class="w-24 font-semibold text-gray-700">중성화 여부:</span>
        <span class="text-gray-600">{{ cat.isNeutered ? 'O' : 'X' }}</span>
      </div>
      <div class="mt-4">
        <h4 class="font-semibold text-gray-700">특이사항:</h4>
        <p class="mt-2 text-gray-600">{{ cat.note || 'Unknown' }}</p>
      </div> 
      <div class="flex items-center">
        <span class="w-24 font-semibold text-gray-700">사진첩:</span>
        <span class="text-gray-600">준비 중입니다.</span>        
      </div>      
      <div class="flex items-center">
        <span class="w-24 font-semibold text-gray-700">동영상:</span>
        <span class="text-gray-600">준비 중입니다.</span>    
      </div>  
    </div>
  </div>  
</template>

<script setup>
import { computed } from 'vue';

defineProps({
  cat: {
    type: Object,
    required: true
  }
});

const getStatusEmoji = (status) => {
  const statusToEmoji = {
    '산냥이': 'ᨒ',
    '집냥이': '🏠',
    '별냥이': '🌈',
    '행방불명': '❓'
  };
  return statusToEmoji[status] || '❓';
};
</script>

<style scoped>
/* Add custom scrollbar styling */
.max-h-[50vh] {
  scrollbar-width: thin;
  scrollbar-color: #CBD5E0 #EDF2F7;
}

/* For Webkit browsers (Chrome, Safari) */
.max-h-[50vh]::-webkit-scrollbar {
  width: 6px;
}

.max-h-[50vh]::-webkit-scrollbar-track {
  background: #EDF2F7;
  border-radius: 3px;
}

.max-h-[50vh]::-webkit-scrollbar-thumb {
  background-color: #CBD5E0;
  border-radius: 3px;
}
</style>