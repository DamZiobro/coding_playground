/*
 * HelloWorld.java
 * Copyright (C) 2017 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class HelloWorld
{
    public static void main(String[] args) {
      AbstractApplicationContext ctx = new ClassPathXmlApplicationContext("beans.xml");
      Greeter greeter = (Greeter) ctx.getBean("greeter");
      System.out.println(greeter.sayHello());
      System.out.println(greeter.saySecondMessage());

      ctx.registerShutdownHook();
    }
}


