/*
 * ShoppingCartTests.java
 */

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import org.junit.Before;
import org.junit.Test;
import com.company.IShoppingCart;
import com.company.ShoppingCart;
import com.company.IProduct;
import com.company.Product;

import java.lang.Double;

public class ShoppingCartTests
{

  private IShoppingCart cart;
  private IProduct product1;
  private IProduct product2;

  @Before
  public void setUp() throws Exception {
    product1 = new Product("newspaper", 1.10, 3);
    product2 = new Product("ice cream", 2.10, 2);
    cart = new ShoppingCart();
  }

  @Test
  public void testAddProduct() {
    cart.addProduct(product1);
    cart.addProduct(product2);
    assertEquals(2, cart.capacity());
  }

  @Test(expected = IllegalArgumentException.class)
  public void testAddNullProduct() {
    cart.addProduct(null);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testAddProductWithNegativePrice() {
    cart.addProduct(new Product("test", -2, 3));
  }

  public void testRemoveProduct() {
    boolean ret = cart.removeProduct(product1);
    assertEquals(true, ret);
  }

  @Test
  public void testRemoveNullProduct() {
    boolean ret = cart.removeProduct(null);
    assertFalse(ret);
  }

  @Test
  public void testClear() {
    cart.clear();
    assertEquals(0, Double.compare(0.0, cart.getTotalPrice()));
  }

  @Test
  public void testUpdateProductQuantity() {
    cart.clear();
    IProduct p =  new Product("test2", 0.50, 5);
    cart.addProduct(p);
    cart.addProduct(p, 3);
    assertEquals(0, Double.compare(4.0, cart.getTotalPrice()));
  }

  @Test
  public void testUpdateProductQuantityNegative() {
    cart.clear();
    IProduct p =  new Product("test2", 0.50, 5);
    cart.addProduct(p);
    cart.addProduct(p, -3);
    assertEquals(0, Double.compare(1.0, cart.getTotalPrice()));
  }

  @Test
  public void testAddProduct2times() {
    cart.clear();
    cart.addProduct(new Product("test2", 0.50, 5));
    cart.addProduct(new Product("test2", 0.50, 5));
    assertEquals(0, Double.compare(5.0, cart.getTotalPrice()));
  }

  @Test
  public void testTotalPrice() {
    cart.clear();
    cart.addProduct(new Product("test", 5.50, 3));
    cart.addProduct(new Product("test2", 0.50, 5));
    cart.addProduct(new Product("test3", 0.30, 1));
    assertEquals(0, Double.compare(19.30, cart.getTotalPrice()));
  }

}
