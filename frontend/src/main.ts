import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
// app.use(router) 之后,vue-router 会向所有组件实例注入两个全局属性:
// $route(当前路由,只读响应式，包含当前路由的信息例如参数)和 $router(路由实例,用于导航，如 push、replace、back)

app.mount('#app')
