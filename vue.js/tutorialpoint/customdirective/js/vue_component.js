/*
 * vue_component.js
 * Copyright (C) 2021 damian <damian@damian-desktop>
 *
 * Distributed under terms of the MIT license.
 */

 Vue.directive("changestyle",{
    bind(e1,binding, vnode) {
       console.log(e1);
       console.log(binding.value.color);
       console.log(vnode);
       e1.style.color=binding.value.color;
       e1.style.fontSize = "30px";
    }
 });
 var vm = new Vue({
    el: '#databinding',
    data: {
    },
    methods : {
    },
 });
