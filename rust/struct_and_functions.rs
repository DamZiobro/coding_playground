fn main() {
   //initialize structure
   let emp1 = Employee{
      company:String::from("TutorialsPoint"),
      name:String::from("Mohtashim"),
      age:50
   };
   let emp2 = Employee {
      company:String::from("TutorialsPoint"),
      name:String::from("Kannan"),
      age:32
   };
   let elder = who_is_elder(emp1,emp2);
   println!("elder is:");

   //prints details of the elder employee
   display(elder);
}
//accepts instances of employee structure and compares their age
fn who_is_elder (emp1:Employee,emp2:Employee)->Employee {
   if emp1.age>emp2.age {
      return emp1;
   } else {
      return emp2;
   }
}
//display name, comapny and age of the employee
fn display( emp:Employee) {
   println!("Name is :{} company is {} age is {}",emp.name,emp.company,emp.age);
}
//declare a structure
struct Employee {
   name:String,
   company:String,
   age:u32
}
