<template>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export const eel = window.eel;
// Expose the `sayHelloJS` function to Python as `say_hello_js`
function sayHelloJS(res_from_py) {
    console.log("res:" + res_from_py);
    //注意:外界js不能直接访问vue methods中的方法,我们这里通过mounted中把js_say_hello_vue赋值为window.j来间接访问js_say_hello_vue
    j(res_from_py)
}
// WARN: must use window.eel to keep parse-able eel.expose{...}
window.eel.expose(sayHelloJS, "say_hello_js");

export default {
  name: 'App',
  components: {
    HelloWorld
  },
    methods: {
        js_say_hello_vue(res_from_py) {
            console.log("methods=>js_say_hello_vue")
            console.log("methods=>res_from_py:",res_from_py)
        }
    },
    mounted: function() {
        //让外界的js可以访问vue methods中的js_say_hello_vue函数
        window.j = this.js_say_hello_vue;
        //call function of py
        eel.hello_world()((val) => {
            console.log(val)     
        })
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
