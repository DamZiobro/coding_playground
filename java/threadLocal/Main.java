/*
 * Main.java
 * Copyright (C) 2020 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

public class Main {
  public static void main(String[] args) {
     new Thread(Main::run).start();
     new Thread(Main::run).start();
     }//from  ww  w .  j a  v  a2s  . co  m
  public static void run() {
     int counter = 3;
     System.out.println(Thread.currentThread().getName()+ "  generated counter:  " + counter);
     for (int i = 0; i < counter; i++) {
        CallTracker.call();
     }
  }
}
class CallTracker {
     private static ThreadLocal<Integer> threadLocal = new ThreadLocal<Integer>();
     public static void call() {
     int counter = 0;
     Integer counterObject = threadLocal.get();

     if (counterObject == null) {
        counter = 1;
     } else {
        counter = counterObject.intValue();
        counter++;
     }
     threadLocal.set(counter);
     String threadName = Thread.currentThread().getName();
     System.out.println("Call  counter for " + threadName + "  = " + counter);
   }
}
