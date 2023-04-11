"use strict";
var myname = "John";
var score1 = 50;
var score2 = 42.50;
var sum = score1 + score2;
//var something:number = "hello" //compilation error as trying to assign string to number
console.log("myname: " + myname);
console.log("first score: " + score1);
console.log("second score: " + score2);
console.log("sum of the scores: " + sum);
//type assertion
var str = '1';
var str2 = str; //str is now of type number 
console.log(typeof (str2));
