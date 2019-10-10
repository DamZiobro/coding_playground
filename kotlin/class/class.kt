class myClass {
   // property (data member)
   private var name: String = "Damian"
   
   // member function
   fun printMe() {
      println("Test printing name: "+name)
   }
}
fun main(args: Array<String>) {
   val obj = myClass() // create obj object of myClass class
   obj.printMe()
}
