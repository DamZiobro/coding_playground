fn main() {
    println!("Hello, world!");
    let version = env!("CARGO_PKG_VERSION");
    println!("version: {:?}", version);
    let my_var = env!("MY_VAR");
    println!("my_var: {:?}", my_var);
    let out_dir = env!("OUT_DIR");
    println!("out_dir: {:?}", out_dir);
}
