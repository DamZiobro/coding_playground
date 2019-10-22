fn main(){
   let data = [10,20,30,40,50];
   use_slice(&data[1..4]);
   //this is effectively borrowing elements for a while
}
fn use_slice(slice:&[i32]) { 
   // is taking a slice or borrowing a part of an array of i32s
   println!("length of slice is {:?}",slice.len());
   println!("{:?}",slice);
}
