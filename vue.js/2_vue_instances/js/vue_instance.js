/*
 * vue_instance.js
 * Copyright (C) 2019 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */
var  vm = new Vue({
   el: '#vue_det',
   data: {
      firstname : "Ria",
      lastname  : "Singh",
      address    : "Mumbai"
   },
   methods: {
      mydetails : function() {
         return "I am "+this.firstname +" "+ this.lastname;
      }
   }
})

