pub mod movies {
   pub fn play(name:String) {
      println!("Playing movie {}",name);
   }
}
use movies::play;
fn main(){
   play("Herold and Kumar ".to_string());
}
