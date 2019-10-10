fun main(args: Array<String>) {
   val demo = Outer().Nested().foo() // calling nested class method
   print(demo)
}
class Outer {
   private val welcomeMessage: String = "Welcome to the Kotlin world"
   inner class Nested {
      fun foo() = welcomeMessage
   }
}
