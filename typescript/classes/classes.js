"use strict";
class Car {
    //constructor 
    constructor(engine) {
        this.engine = engine;
    }
    //function 
    disp() {
        console.log("Function displays Engine is  :   " + this.engine);
    }
}
//create an object 
var car = new Car("XXSY1");
//access the field 
console.log("Reading attribute value Engine as :  " + car.engine);
//access the function
car.disp();
// INHERITANCE
class Shape {
    constructor(a) {
        this.Area = a;
    }
}
class Circle extends Shape {
    disp() {
        console.log("Area of the circle:  " + this.Area);
    }
}
var circle = new Circle(223);
circle.disp();
/// METHOD OVERWRITING
class PrinterClass {
    doPrint() {
        console.log("doPrint() from Parent called?");
    }
}
class StringPrinter extends PrinterClass {
    doPrint() {
        super.doPrint();
        console.log("doPrint() is printing a string?");
    }
}
var obj = new StringPrinter();
obj.doPrint();
