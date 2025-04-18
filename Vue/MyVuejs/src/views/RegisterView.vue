<template >
    <div>
<main class="form-signin w-25 m-auto">
  <form>
    <h1 class="h3 mb-3 fw-normal mt-3">Please register</h1>
    <div class="form-floating">
      <Input :type="`text`" :placeholder="`Your name`" :label="`Name`"/>

    </div>
    
    <div class="form-floating mt-3">
      <Input :type="`email`" :placeholder="`Your email`" :label="`Email`"/>
    
    </div>
    
    <div class="form-floating mt-3">
    <Input :type="`password`" :placeholder="`Your password`" :label="`Password`"/>
    
    </div>
    <Button type="submit"  @click="submitHandler">Register</Button>
    
  </form>
</main>
</div>
</template>
<script>
import Button from '@/components/ui-components/Button.vue';
import Input from '@/components/ui-components/Input.vue';
export default {
 name: 'RegisterView',
 data() {
   return {
     // Define your data properties here
   };
 },   
 computed: {
    isloading(){
      return  this.$store.state.auth.isloading;
    }
 },
 methods:{
  submitHandler(e){
    e.preventDefault();
    this.$store.commit(`setloading`);
  }
 }
}
</script>
<style >
    
</style>