/*
 * Greeter.java
 * Copyright (C) 2017 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

public class Greeter
{
  String message;
  String secondMessage;
  public Greeter(String message) {
    this.message = message;
  }

  public void setSecondMessage(String secondMessage) {
    this.secondMessage = secondMessage; 
  }

  public String sayHello(){
    return message; 
  }
  
  public String saySecondMessage(){
    return secondMessage; 
  }
}


