/*
 * vue_instance.js
 * Copyright (C) 2019 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

var vm = new Vue({
   el: '#computed_props',
   data: {
      firstname :"",
      lastname :"",
      birthyear : ""
   },
   computed :{
      getfullname : function(){
         return this.firstname +" "+ this.lastname;
      }
   }
})
