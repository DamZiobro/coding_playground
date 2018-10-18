/*
 * ProductTests.java
 */

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import org.junit.Before;
import org.junit.Test;
import com.company.IProduct;
import com.company.Product;

import java.lang.Double;
import java.lang.IllegalArgumentException;

public class ProductTests
{

  private IProduct product;

  @Before
  public void setUp() throws Exception {
    product = new Product("Ice Cream", 5.50);
  }

  @Test
  public void testSetProperPrice() {
    product.setPrice(6.00);
    assertEquals(0, Double.compare(6.00, product.getPrice()));
  }

  @Test
  public void testSetZeroPrice() {
    product.setPrice(0.00);
    assertEquals(0, Double.compare(0.00, product.getPrice()));
  }

  @Test
  public void testSetIntPrice() {
    product.setPrice(10);
    assertEquals(0, Double.compare(10.00, product.getPrice()));
  }

  @Test(expected = IllegalArgumentException.class)
  public void testSetEmptyName() {
    product.setName("");
  }

  @Test
  public void testSetProperName() {
    product.setName("Ice");
    assertTrue(product.getName().equals("Ice"));
  }

  @Test(expected = IllegalArgumentException.class)
  public void testSetNullName() {
    product.setName(null);
  }

  @Test
  public void testProductOnlyConstructor() {
    product = new Product("Ice Cream", 10);
    assertEquals(1, product.getQuantity());
  }

  @Test
  public void testQuantityConstructor() {
    product = new Product("Ice Cream", 5.50, 5);
    assertEquals(5, product.getQuantity());
  }

  @Test(expected = IllegalArgumentException.class)
  public void testNegativeQuantity() {
    product.setQuantity(-1);
  }

  @Test
  public void testGetTotalPrice() {
    product = new Product("newspaper", 10.0, 3);
    assertEquals(0, Double.compare(product.getTotalPrice(),30.0));
  }

}


