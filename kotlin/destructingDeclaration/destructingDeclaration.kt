fun main(args: Array<String>) {
   val s = Student("TutorialsPoint.com","Kotlin")
   val (name,subject) = s
   println("You are learning "+subject+" from "+name)
}
data class Student( val a :String,val b: String ){
   var name:String = a
   var subject:String = b
}
