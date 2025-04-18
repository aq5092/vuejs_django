<template >
    <div class="d-flex flex-column flex-md-row align-items-center pb-3 mb-4 border-bottom">
      <a  class="d-flex align-items-center text-dark text-decoration-none " @click="$router.push('/')">
        
        <span class="fs-4 cursor-pointer">Django-Vuejs </span>
      </a>

      <nav class="d-inline-flex mt-2 mt-md-0 ms-md-auto">
        <a  ><RouterLink class="me-3 py-2 text-dark text-decoration-none" :to="{name:`register`}"> Register</RouterLink></a>
        <a  ><RouterLink class="me-3 py-2 text-dark text-decoration-none" :to="{name:`login`}"> Login</RouterLink></a>
      </nav>
    </div>
</template>
<script>
import { logo } from './constants';

logo
export default {
    
 data   () {
    return {
     logo: logo, 
        // Add your data properties here
    }
  },
  methods: {
    // Add your methods here
  },
  mounted() {
    // Code to run when the component is mounted
  }   
}
</script>
<style >
    
</style>