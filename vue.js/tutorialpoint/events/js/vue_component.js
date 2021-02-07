/*
 * vue_component.js
 * Copyright (C) 2021 damian <damian@damian-desktop>
 *
 * Distributed under terms of the MIT license.
 */
 var vm = new Vue({
    el: '#databinding',
    data: {
       num1: 100,
       num2 : 200,
       total : ''
    },
    methods : {
       displaynumbers : function(event) {
          console.log(event);
          return this.total =  this.num1+ this.num2;
       }
    },
 });
