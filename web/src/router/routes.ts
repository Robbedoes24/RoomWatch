import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/IndexPage.vue') }],
  },
  {
    path: '/roomselector',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/RoomSelector.vue') }],
  },

  {
    path: '/camerasetup',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/CameraSetup.vue') }],
  },
];

export default routes;
