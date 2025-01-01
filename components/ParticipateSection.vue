<template>
    <div class="max-w-2xl mx-auto p-6">
      <h4 class="text-xl font-bold text-center mb-8">고양이들 돌보기 또는 입양, 중성화 등을 통한 개체 수 조절에
         동참을 원하시면 아래 서식을 작성해 주세요</h4>
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Name Input -->
        <div>
          <label class="block text-gray-700 mb-2">이름</label>
          <input 
            v-model="name"
            type="text" 
            required
            class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-yellow-400 outline-none"
          >
        </div>

  
        <!-- Phone Input -->
        <div>
          <label class="block text-gray-700 mb-2">전화번호</label>
          <input 
            v-model="phone"
            type="phone" 
            required
            class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-yellow-400 outline-none"
          >
        </div>        

        <!-- Email Input -->
        <div>
          <label class="block text-gray-700 mb-2">이메일</label>
          <input 
            v-model="email"
            type="email"             
            class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-yellow-400 outline-none"
          >
        </div>
  
        <!-- Message Input -->
        <div>
          <label class="block text-gray-700 mb-2">메시지</label>
          <textarea 
            v-model="message"
            rows="4"
            required
            class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-yellow-400 outline-none"
          ></textarea>
        </div>
  
        <!-- Submit Button -->
        <button 
            type="submit"
            :disabled="isSubmitting"
            class="w-full py-3 bg-gradient-to-r from-yellow-400 to-orange-300 text-black rounded-lg font-bold hover:shadow-lg transition-all duration-200"
            >
            {{ isSubmitting ? '제출 중...' : '제출하기' }}
        </button>

        <!-- Status Message -->
        <div 
            v-if="statusMessage" 
            :class="isError ? 'text-red-600' : 'text-green-600'"
            class="text-center mt-4 font-medium"
            >
            {{ statusMessage }}
        </div>
      </form>
    </div>
</template>


<script setup>
    import { ref } from 'vue'
    import { collection, addDoc } from 'firebase/firestore'
    import { initializeFirebase } from '~/utils/firebase'

    const { db } = initializeFirebase()

    const name = ref('')
    const phone = ref('')
    const email = ref('')
    const message = ref('')

    const isSubmitting = ref(false)
    const statusMessage = ref('')
    const isError = ref(false)

    const handleSubmit = async () => {
    isSubmitting.value = true
    statusMessage.value = ''
    isError.value = false

    try {
        await addDoc(collection(db, 'contacts'), {
        name: name.value,
        phone: phone.value,
        email: email.value,
        message: message.value,
        createdAt: new Date()
        })
        
        // Clear form
        name.value = ''
        phone.value = ''
        email.value = ''
        message.value = ''
        
        statusMessage.value = '메시지가 전송되었습니다. 감사합니다!'
    } catch (error) {
        console.error('Error submitting form:', error)
        isError.value = true
        statusMessage.value = '죄송합니다. 다시 시도해 주세요.'
    } finally {
        isSubmitting.value = false
    }
    }
</script>