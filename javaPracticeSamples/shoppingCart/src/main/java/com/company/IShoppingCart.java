/*
 * IShoppingCart.java
 * Copyright (C) 2018 damian <damian@C-DZ-E5500>
 *
 * Distributed under terms of the MIT license.
 */
package com.company;

import com.company.IProduct;

public interface IShoppingCart
{
  public void addProduct(IProduct product);
  public void addProduct(IProduct product, int quantity);
  public boolean removeProduct(IProduct product);
  public void printCart();
  public void clear();
  public double getTotalPrice();
  public int capacity();
}


