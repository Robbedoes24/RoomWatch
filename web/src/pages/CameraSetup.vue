<script setup lang="ts"></script>
<template>
  <q-layout class="flex flex-center column q-pb-md">
    <h1 style="">Camera view</h1>
    <!-- add button to go back -->
    <q-card class="cardSize" :bordered="true">
      <embed type="text/html" src="snippet.html" width="100%" height="100%" />
    </q-card>
  </q-layout>
</template>

<style lang="scss">
.cardSize {
  width: 600px;
  height: 600px;

  border: 10px dotted $blue-10;
}
</style>
