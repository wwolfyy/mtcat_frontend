import { ref, onMounted, onUnmounted } from 'vue'

export function useViewport() {
  const width = ref(0)
  const isMobile = ref(false)

  const updateWidth = () => {
    width.value = window.innerWidth
    isMobile.value = width.value < 768 // breakpoint for mobile
  }

  onMounted(() => {
    updateWidth()
    window.addEventListener('resize', updateWidth)
  })

  onUnmounted(() => {
    window.removeEventListener('resize', updateWidth)
  })

  return {
    width,
    isMobile
  }
}