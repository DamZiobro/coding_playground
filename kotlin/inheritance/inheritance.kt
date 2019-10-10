import java.util.Arrays

//Everything in Kotlin is by default final, hence, we need to use 
//the keyword “open” in front of the class declaration 
//to make it allowable to inherit.
open class ABC {
   open fun think () {
      println("Hey!! i am thinking ")
   }
}
class BCD: ABC() { // inheritance happens using default constructor 
   override fun think() {
      println("I Am from Child")
   }
}
fun main(args: Array<String>) {
   var  a = BCD()
   a.think()
}
