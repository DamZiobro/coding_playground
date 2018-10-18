/*
 * ShoppingCart.java
 * Copyright (C) 2018 damian <damian@C-DZ-E5500>
 *
 * Distributed under terms of the MIT license.
 */
package com.company;

import com.company.IShoppingCart;
import com.company.IProduct;
import java.util.List;
import java.util.ArrayList;
import java.lang.Double;
import java.math.BigDecimal;
import java.lang.StringBuilder;

public class ShoppingCart implements IShoppingCart
{
  protected List<IProduct> items;

	public ShoppingCart() {
    this.items = new ArrayList<IProduct>();
	}

  public void addProduct(IProduct product) throws IllegalArgumentException {
    if (product == null) {
      throw new IllegalArgumentException("product cannot be null");
    }
    this.addProduct(product, product.getQuantity());
  }

  public void addProduct(IProduct product, int quantity) throws IllegalArgumentException {
    IProduct p = getProductFromItems(product);
    if (p == null) {
      product.setQuantity(quantity);
      this.items.add(product);
    } else {
      p.setQuantity(p.getQuantity() + quantity);
    }
  }

  public boolean removeProduct(IProduct product) {
    return this.items.remove(product);
  }

  public void printCart() {
    System.out.println(this.toString());
  }

  public String toString() {
    StringBuilder s = new StringBuilder();
    for (IProduct p : this.items) {
      s.append( " * " + p.toString() + "\n");
    }
    s.append("------\n");
    s.append("Total Price: " + this.getTotalPrice());
    return s.toString();
  }

  public void clear() {
    this.items.clear();
  }

  public double getTotalPrice() {
    double total = 0.0;
    for (IProduct p : this.items) {
      total += (p.getPrice() * p.getQuantity());
    }
    return total;
  }

  protected IProduct getProductFromItems(IProduct product){
    int index = this.items.indexOf(product);
    IProduct p = null;
    if (index != -1) {
      p = this.items.get(index);
    }
    return p;
  }

  public int capacity() {
    return this.items.size();
  }

}


