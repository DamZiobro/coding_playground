/*
 * PrimeFactors.java
 * Copyright (C) 2018 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

package com.company;

import java.util.List;
import java.util.ArrayList;
import java.lang.Integer;

public class PrimeFactors
{
	public PrimeFactors() {
		
	}

  public List<Integer> generate(int n) {
    List<Integer> primes = new ArrayList<Integer>();
    int candidate = 2;
    while (n > 1) {
      while (n % candidate == 0) {
        primes.add(candidate);
        n /= candidate;
      }
      candidate++;
    }
    return primes;
  }

}


