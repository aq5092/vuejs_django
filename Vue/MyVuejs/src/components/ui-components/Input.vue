<template lang="">
    <div class="form-floating mt-3">
      <input :type="type" :label="label" class="form-control" id="floatingPassword" :placeholder="plaseholder">
      <label for="floatingPassword">{{label}}</label>
    </div>
</template>
<script>
export default {
    name: 'Input',
    props: {
        label: String,
        type: String,
        placeholder: String,
    },
}
</script>
<style lang="">
    
</style>