/*
 * Account.java
 */

package com.company;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class Account
{
  private BigDecimal amount;

	public Account(BigDecimal amount) throws IllegalArgumentException {
    if (amount.compareTo(new BigDecimal("0.00")) < 0) {
      throw new IllegalArgumentException();
    }
    this.amount = amount;
  }

  public BigDecimal getInterest(){
    if (this.amount.compareTo(new BigDecimal("999.99")) <= 0) 
    {
      return this.amount.multiply(new BigDecimal("0.01")).setScale(2,RoundingMode.HALF_EVEN);
    } else if (this.amount.compareTo(new BigDecimal("4999.99")) <= 0)  {
      return this.amount.multiply(new BigDecimal("0.02")).setScale(2,RoundingMode.HALF_EVEN);
    } else {
      return this.amount.multiply(new BigDecimal("0.03")).setScale(2,RoundingMode.HALF_EVEN);
    }
  }

}


