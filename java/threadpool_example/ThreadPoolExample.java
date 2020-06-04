/*
 * Task.java
 * Copyright (C) 2020 damian <damian@damian-desktop>
 *
 * Distributed under terms of the MIT license.
 *
 * Java program to illustrate ThreadPool 
 */

import java.text.SimpleDateFormat;  
import java.util.Date; 
import java.util.concurrent.ExecutorService; 
import java.util.concurrent.Executors; 
import java.util.List;
import java.util.ArrayList;
  
// Task class to be executed (Step 1) 
class Task implements Runnable    
{ 
    private String name; 
      
    public Task(String s) 
    { 
        name = s; 
    } 
      
    // Prints task name and sleeps for 1s 
    // This Whole process is repeated 5 times 
    public void run() 
    { 
        try
        { 
            for (int i = 0; i<=5; i++) 
            { 
                if (i==0) 
                { 
                    Date d = new Date(); 
                    SimpleDateFormat ft = new SimpleDateFormat("hh:mm:ss"); 
                    System.out.println("Initialization Time for"
                            + " task name - "+ name +" = " +ft.format(d));    
                    //prints the initialization time for every task  
                } 
                else
                { 
                    Date d = new Date(); 
                    SimpleDateFormat ft = new SimpleDateFormat("hh:mm:ss"); 
                    System.out.println("Executing Time for task name - "+ 
                            name +" = " +ft.format(d));    
                    // prints the execution time for every task  
                } 
                Thread.sleep(1000); 
            } 
            System.out.println(name+" complete"); 
        } 
          
        catch(InterruptedException e) 
        { 
            e.printStackTrace(); 
        } 
    } 
} 
public class ThreadPoolExample
{ 
     // Maximum number of threads in thread pool 
    static final int MAX_THREADS = 300;              
  
    public static void main(String[] args) 
    { 
        // creates five tasks 
        List<Task> tasks = new ArrayList<Task>();
        for (int i = 0; i < 300; i++) {
           tasks.add(new Task("task" + i));
        }
          
        // creates a thread pool with MAX_T no. of  
        // threads as the fixed pool size(Step 2) 
        ExecutorService pool = Executors.newFixedThreadPool(MAX_THREADS);   
         
        // passes the Task objects to the pool to execute (Step 3) 
        for (Task task : tasks){
            pool.execute(task);
        }
          
        // pool shutdown ( Step 4) 
        pool.shutdown();     
    } 
} 

