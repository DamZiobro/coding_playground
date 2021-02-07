/*
 * vue_component.js
 * Copyright (C) 2021 damian <damian@damian-desktop>
 *
 * Distributed under terms of the MIT license.
 */
 var vm = new Vue({
    el: '#computed_props',
    data: {
       kilometers : 0,
       meters:0
    },
    methods: {
    },
    computed :{
    },
    watch : {
       kilometers:function(val) {
          this.kilometers = val;
          this.meters = val * 1000;
       },
       meters : function (val) {
          this.kilometers = val/ 1000;
          this.meters = val;
       }
    }
 });
