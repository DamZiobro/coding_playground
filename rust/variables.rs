fn main() {
   let company_string = "TutorialsPoint";  // string type
   let rating_float = 4.5;                 // float type
   let is_growing_boolean = true;          // boolean type
   let icon_char = '♥';                    //unicode character type
   let str_literal:&str = "String literal";//String literal
   let str_object_empty = String::new();   //String empty object
   let str_object_non_empty = String::from("String object");   //String non-emty object 

   println!("company name is:{}",company_string);
   println!("company rating on 5 is:{}",rating_float);
   println!("company is growing :{}",is_growing_boolean);
   println!("company icon is:{}",icon_char);
   println!("string literal is:{}",str_literal);
   println!("string object empty is:{}",str_object_empty);
   println!("string object non-empty is:{}",str_object_non_empty);
}
