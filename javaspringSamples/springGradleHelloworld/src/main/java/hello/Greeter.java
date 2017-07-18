/*
 * Greeter.java
 * Copyright (C) 2017 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

public class Greeter
{
  String message;
  public Greeter(String message) {
    this.message = message;
  }
  public String sayHello(){
    return message; 
  }
}


