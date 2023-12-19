<!-- DotInfoCard.vue -->
<template>
  <q-card>
    <q-card-section class="q-pt-md">
      <q-card-title> Local: {{ props.id }} </q-card-title>
    </q-card-section>

    <q-card-section>
      <p>Number of Students: {{ props.numStudents }}</p>
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
  widows: 230px;
  height: 100px;
}
</style>
