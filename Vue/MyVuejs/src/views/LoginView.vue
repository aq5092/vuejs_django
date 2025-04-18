<template >
    <div>
<main class="form-signin w-25 m-auto">
  <form>
    <h1 class="h3 mb-3 fw-normal mt-3">Login</h1>
    
    <div class="form-floating mt-3">
      <Input :type="`email`" :placeholder="`email`" :label="`Email`"/>
    
    </div>
    <Input :type="`password`" :placeholder="`password`" :label = "`Password`"/>
    <Button type="submit">Login</Button>
  </form>
</main>
</div>
</template>
<script>
import Input from '@/components/ui-components/Input.vue';
import Button from '@/components/ui-components/Button.vue';
export default {
 name: 'LoginView',
 data() {
   return {
     // Define your data properties here
   };
 },   
}
</script>
<style >
    
</style>