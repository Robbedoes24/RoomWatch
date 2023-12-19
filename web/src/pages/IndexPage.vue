<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();
function freeRoomsButton() {
  // Go to free rooms page

  router.push('/roomselector');
  return;
}

function setupButton() {
  // Go to setup page
  router.push('/camerasetup');
  return;
}
</script>
<template>
  <q-layout class="column flex-center">
    <q-card class="my-card column">
      <q-btn class="q-mb-md" size="50px" @click="freeRoomsButton">
        Free rooms
      </q-btn>
      <q-btn size="50px" @click="setupButton">Setup</q-btn>
    </q-card>
  </q-layout>
</template>

<style lang="scss" scoped>
.my-card {
  width: 100%;
  max-width: 450px;
}
</style>
