fun main(args: Array<String>) {
   val mylambda:(String)->Unit  = {s:String->print(s)}
   val v:String = "TutorialsPoint.com"
   myFun(v,mylambda) //passing lambda as a parameter of another function 
}
fun myFun(a :String, action: (String)->Unit) { //passing lambda 
   print("Heyyy!!!")
   action(a)// call to lambda function
}
