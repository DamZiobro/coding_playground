/*
 * vue_instance.js
 * Copyright (C) 2019 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

var vm = new Vue({
   el: '#databinding',
   data: {
     num1: 100,
     num2: 200,
     total: ''
   },
   methods : {
     displaynumbers : function(event) {
       console.log(event);
       this.num1 = this.num1 + this.num2;
       return this.total = this.num1 + this.num2;
     }
   }
})
