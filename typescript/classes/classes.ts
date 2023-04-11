class Car { 
   //field 
   engine:string; 
   
   //constructor 
   constructor(engine:string) { 
      this.engine = engine 
   }  
   
   //function 
   disp():void { 
      console.log("Function displays Engine is  :   "+this.engine) 
   } 
} 

//create an object 
var car = new Car("XXSY1")

//access the field 
console.log("Reading attribute value Engine as :  "+car.engine)  

//access the function
car.disp()

// INHERITANCE

class Shape { 
   Area:number 
   
   constructor(a:number) { 
      this.Area = a 
   } 
} 

class Circle extends Shape { 
   disp():void { 
      console.log("Area of the circle:  "+this.Area) 
   } 
}
  
var circle = new Circle(223); 
circle.disp()

/// METHOD OVERWRITING
class PrinterClass { 
   doPrint():void {
      console.log("doPrint() from Parent called?") 
   } 
} 

class StringPrinter extends PrinterClass { 
   doPrint():void { 
      super.doPrint() 
      console.log("doPrint() is printing a string?")
   } 
} 

var obj = new StringPrinter() 
obj.doPrint()
