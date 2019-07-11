/*
 * AccountTests.java
 */
package com.company;

import static org.junit.Assert.assertEquals;
import org.junit.Before;
import org.junit.Test;
import com.company.Account;
import java.math.BigDecimal;

public class AccountTests
{

  private Account account;

  @Test
  public void testZero() {
    account = new Account(new BigDecimal(0));
    assertEquals(new BigDecimal("0.00"), account.getInterest());
  }

  @Test
  public void test999() {
    account = new Account(new BigDecimal("999.99"));
    assertEquals(new BigDecimal("10.00"), account.getInterest());
  }

  @Test
  public void test998() {
    account = new Account(new BigDecimal("998.50"));
    assertEquals(new BigDecimal("9.98"), account.getInterest());
  }

  @Test
  public void test432() {
    account = new Account(new BigDecimal("432.00"));
    assertEquals(new BigDecimal("4.32"), account.getInterest());
  }

  @Test
  public void test1000() {
    account = new Account(new BigDecimal("1000.00"));
    assertEquals(new BigDecimal("20.00"), account.getInterest());
  }

  @Test
  public void test4999edge() {
    account = new Account(new BigDecimal("4999.99"));
    assertEquals(new BigDecimal("100.00"), account.getInterest());
  }

  @Test
  public void test3200() {
    account = new Account(new BigDecimal("3200.00"));
    assertEquals(new BigDecimal("64.00"), account.getInterest());
  }

  @Test
  public void test5000edge() {
    account = new Account(new BigDecimal("5000.00"));
    assertEquals(new BigDecimal("150.00"), account.getInterest());
  }

  @Test(expected = IllegalArgumentException.class)
  public void testNegativeAmount() {
    account = new Account(new BigDecimal("-100.00"));
  }

}


