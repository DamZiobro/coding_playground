/*
 * Main.java
 */

package com.company;

import com.company.PrimeFactors;

public class Main
{
  public static void main (String[] args) {
    PrimeFactors calc = new PrimeFactors();

    System.out.println("primeFactors: " + calc.generate(10));
  }
}


