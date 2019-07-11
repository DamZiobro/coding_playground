/*
 * Main.java
 */

package com.company;

import com.company.IProduct;
import com.company.Product;

public class Main
{
  public static void main (String[] args) {
    IShoppingCart cart = new ShoppingCart();
    cart.addProduct(new Product("Ice Cream", 6.00, 2));
    cart.addProduct(new Product("Newspaper", 1.00, 3));
    cart.addProduct(new Product("Knife", 8.00, 1));
    cart.addProduct(new Product("Can of Coke", 0.50, 1));

    cart.printCart();

    //cart.addProduct(new Product("newspaper", 6.00, -2));
  }

}


