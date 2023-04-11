// Example custom build script.
use std::env;
use dotenv::dotenv;

fn main() {
    dotenv().ok();

    println!("cargo:rustc-env=MY_VAR={:}", env::var("MY_VAR").unwrap());
}
