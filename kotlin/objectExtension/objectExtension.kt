fun main(args: Array<String>) {
   println("Heyyy!!! "+A.show())
}

//'companion object' is another mechanism to implement static functionality of Java in Kotlin
class A {
   companion object {
      fun show():String {
         return("You are learning Kotlin")
      }
   }
}
