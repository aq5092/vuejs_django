<template lang="">
    <div>
        Home {{count}}
        <Button @click="$store.commit('increment')">Increment</Button>
        <Button @click="$store.commit('decrement')">Decrement</Button>
        <Button @click="$store.commit('reset')">Reset</Button>
</div>
</template>
<script>
import Button from '@/components/ui-components/Button.vue';
export default {
    computed: {
        count() {
            return this.$store.state.count;
        }
    },
    components: {
        Button
    },
    name: 'HomeView',
}
</script>
<style lang="">
    
</style>