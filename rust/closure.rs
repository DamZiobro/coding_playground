fn main(){
   let is_even = |x| {
      x%2==0
   };
   let no = 13;
   println!("{} is even ? {}",no,is_even(no));
}
