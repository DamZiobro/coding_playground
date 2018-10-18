/*
 * Product.java
 * Copyright (C) 2018 damian <damian@C-DZ-E5500>
 *
 * Distributed under terms of the MIT license.
 */
package com.company;

import com.company.IProduct;
import java.lang.Double;
import java.lang.Integer;
import java.lang.IllegalArgumentException;

public class Product implements IProduct
{

  protected String name;
  protected double price;
  protected int quantity;

  public Product(String name, double price) {
    this(name, price, 1);
  }

	public Product(String name, double price, int quantity) {
	  this.setName(name);
	  this.setPrice(price);
    this.setQuantity(quantity);
	}

  @Override
  public void setName(String name) throws IllegalArgumentException {
    if (name == null || name.equals("")){
      throw new IllegalArgumentException("incorrect 'name' value name=" + name);
    }
    this.name = name;
  }

  @Override
  public void setPrice(double price) throws IllegalArgumentException{
    if(price < 0.0) {
      throw new IllegalArgumentException("incorrect 'price' value price=" + Double.toString(price));
    }
    this.price = price;
  }

  @Override
  public double getPrice() {
    return this.price;
  }

  @Override
  public String getName() {
    return this.name;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder("");

    s.append("Product( name=");
    s.append(this.name);
    s.append(", price=");
    s.append(Double.toString(this.price));
    s.append(", quantity=");
    s.append(Integer.toString(this.quantity));
    s.append(" )");

    return s.toString();
  }

  @Override
  public void setQuantity(int quantity) throws IllegalArgumentException {
    if (quantity < 0) {
      throw new IllegalArgumentException("incorrect 'quantity' value quantity=" + Integer.toString(quantity));
    }
    this.quantity = quantity;
  }

  @Override
  public int getQuantity() {
    return this.quantity;
  }

  @Override
  public double getTotalPrice() {
    return this.price * this.quantity;
  }

}


