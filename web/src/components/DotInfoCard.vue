<!-- DotInfoCard.vue -->
<template>
  <q-card>
    <q-card-section class="q-pt-md">
      <h5>Local: {{ props.id }}</h5>

      <h5>Students: {{ props.numStudents }}</h5>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { ref, watch } from 'vue';

const selectedDot = ref({ id: null, numStudents: null });
const props = defineProps(['id', 'numStudents']);
watch(
  () => selectedDot.value,
  (newVal) => {
    if (newVal.id !== null) {
      // Fetch and set the number of students based on the selectedDot.id
      // Make API call to set the value.
      selectedDot.value.numStudents = 42;
    }
  }
);
</script>

<style lang="scss" scoped>
/* Add styles as needed */
.q-card {
  width: 300px;
  height: 200px;
}
</style>
