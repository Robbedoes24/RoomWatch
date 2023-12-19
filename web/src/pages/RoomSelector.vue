<!-- Your main template -->
<template>
  <q-page
    class="fit column no-wrap justify-start items-start content-start no-scroll"
  >
    <q-card
      class="flex column floorSelector q-pa-md floorCard"
      style="margin-left: 10%; margin-top: 5%; position: absolute"
    >
      <q-btn
        color="grey-5"
        disable
        class="q-mb-md floorBtn"
        size="40px"
        @click="selectFloor(1)"
        >Floor 1</q-btn
      >
      <q-btn
        color="grey-5"
        disable
        class="q-mb-md floorBtn"
        size="40px"
        @click="selectFloor(2)"
        >Floor 2</q-btn
      >
      <q-btn color="grey-6" size="40px" @click="selectFloor(3)">Floor 3</q-btn>
    </q-card>
    <q-card class="self-center" style="margin-top: 5%">
      <q-img
        src="../assets/floor3-1.png"
        width="1200px"
        height="1000px"
      ></q-img>
      <div
        v-for="dot in dots"
        :key="dot.id"
        class="clickable-dot"
        :style="{
          left: dot.position.x + 'px',
          top: dot.position.y + 'px',
          background: dot.color,
        }"
        @click="toggleDotColor(dot)"
      ></div>
    </q-card>

    <DotInfoCard
      v-if="selectedDot.id !== null"
      :id="selectedDot.id"
      :num-students="selectedDot.amountStudent"
      class="self-end justify-start infoCard"
    />
  </q-page>
</template>

<script setup>
import { ref } from 'vue';
import DotInfoCard from 'src/components/DotInfoCard.vue';

const socket = new WebSocket('ws://localhost:8080/');
const selectedDot = ref({ id: null, amountStudent: null });

socket.onopen = () => {
  console.log('WebSocket connection opened');
};

socket.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log('Received message from server:', message);

  const dot = dots.value.find((d) => d.id === message.topic);
  if (dot) {
    dot.amountStudent = message.people;
    dot.color = 'green';
  }
};

socket.onclose = () => {
  console.log('WebSocket connection closed');
};

const dots = ref([
  // A Right side
  {
    id: 'A305',
    position: { x: 1070, y: 400 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'A303',
    position: { x: 1070, y: 500 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'A307',
    position: { x: 1070, y: 300 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'A301',
    position: { x: 1070, y: 600 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'A309',
    position: { x: 1070, y: 200 },
    color: 'red',
    amountStudent: 0,
  },

  // A Left Side
  {
    id: 'A308',
    position: { x: 905, y: 200 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'A306',
    position: { x: 905, y: 300 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'A304',
    position: { x: 905, y: 400 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'A302',
    position: { x: 905, y: 500 },
    color: 'red',
    amountStudent: 0,
  },

  // B Right side
  {
    id: 'B305',
    position: { x: 670, y: 400 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'B303',
    position: { x: 670, y: 500 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'B307',
    position: { x: 670, y: 300 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'B301',
    position: { x: 670, y: 600 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'B309',
    position: { x: 670, y: 200 },
    color: 'red',
    amountStudent: 0,
  },

  // B Left side
  {
    id: 'B308',
    position: { x: 510, y: 200 },
    color: 'red',
    amountStudent: 0,
  },

  {
    id: 'B306',
    position: { x: 510, y: 300 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'B304',
    position: { x: 510, y: 400 },
    color: 'red',
    amountStudent: 0,
  },
  {
    id: 'B302',
    position: { x: 510, y: 500 },
    color: 'red',
    amountStudent: 0,
  },
]);

const toggleDotColor = (dot) => {
  // Update selectedDot directly with the clicked dot information
  selectedDot.value.id = dot.id;
  selectedDot.value.amountStudent = dot.amountStudent;
};

const selectFloor = (floorNumber) => {
  // Logic to handle floor selection
  console.log(`Selected Floor ${floorNumber}`);
};
</script>

<style lang="scss">
.clickable-dot {
  position: absolute;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  cursor: pointer;
}

.infoCard {
  position: absolute;
  width: 200px;
  right: 600px;
  top: 200px;
}

.floorCard {
  background-color: $grey-3;
}
</style>
