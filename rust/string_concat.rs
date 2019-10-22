fn main(){
   let n1 = "Tutorials".to_string();
   let n2 = "Point".to_string();

   let n3 = n1 + &n2; // n2 reference is passed because operator+ uses add function with signature add(self, &str)
   println!("{}",n3);
}
