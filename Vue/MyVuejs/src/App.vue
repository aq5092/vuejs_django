<template >
  <div>
    <div class="container">
    <Navbar />
    <RouterView />

  </div>

  </div>
</template>
<script>
import { RouterView } from 'vue-router';
import Navbar from './components/Navbar.vue';
export default {
  components: {
    // Add your components here
  Navbar,
  },
}
</script>
<style >
  
</style>