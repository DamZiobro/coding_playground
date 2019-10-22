//declare a structure
struct Point {
   x: i32,
   y: i32,
}
impl Point {
   //static method that creates objects of the Point structure
   fn get_instance(x: i32, y: i32) -> Point {
      Point { x: x, y: y }
   }
   //display values of the structure's field
   fn display(&self){
      println!("x ={} y={}",self.x,self.y );
   }
}
fn main(){
   // Invoke the static method
   let p1 = Point::get_instance(10,20);
   p1.display();
}
