struct User {
    name: String,
    age: i32
}

impl User {
    fn check_name(&mut self){
        self.name = String::from("Anthony");
        println!("New name: {}", self.name);
    }
}

//

fn main() {
    let mut text: String = String::from("username");
    println!("{}", text);

    text = String::from("tests");
    println!("{}", text);

    let theta: &str = "fasdfasfd";
    println!("{}", &theta);

    let mut a = User{name: String::from("Andrew"), age: 25};
    println!("name: {}\nage: {}", a.name, a.age);
    a.check_name();
    println!("name: {}\nage: {}", a.name, a.age);
}
