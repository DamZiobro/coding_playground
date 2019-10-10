fun main(args: Array<String>) {
   val HUman = HUman("TutorialsPoint.com", 25)
   print("${HUman.message}"+"${HUman.firstName}"+
      "Welcome to the example of Secondary  constructor, Your Age is-${HUman.age}")
}
class HUman(val firstName: String, var age: Int) {
   val message:String  = "Hey!!!"
      constructor(name : String , age :Int ,message :String):this(name,age) {
   }
}
