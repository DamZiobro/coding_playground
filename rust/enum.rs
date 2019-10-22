// The `derive` attribute automatically creates the 
//implementation
// required to make this `enum` printable with 

#[derive(Debug)]
enum GenderCategory {
   Male,Female
}

// The `derive` attribute automatically creates the implementation
// required to make this `struct` printable with `fmt::Debug`.
#[derive(Debug)]
struct Person {
   name:String,
   gender:GenderCategory
}

fn main() {
   let p1 = Person {
      name:String::from("Mohtashim"),
      gender:GenderCategory::Male
   };
   let p2 = Person {
      name:String::from("Amy"),
      gender:GenderCategory::Female
   };
   println!("{:?}",p1);
   println!("{:?}",p2);
}
