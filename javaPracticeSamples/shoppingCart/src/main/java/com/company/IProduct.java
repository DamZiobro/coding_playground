/*
 * IProduct.java
 */

package com.company;

public interface IProduct
{
 
  public String getName();
  public double getPrice();
  public int getQuantity();

  public void setName(String name);
  public void setPrice(double price);
  public void setQuantity(int price);

  public double getTotalPrice();
}


