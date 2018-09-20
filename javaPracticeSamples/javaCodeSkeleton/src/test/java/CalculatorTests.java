/*
 * CalculatorTests.java
 */

import static org.junit.Assert.assertEquals;
import org.junit.Before;
import org.junit.Test;
import com.company.Calculator;

public class CalculatorTests
{

  private Calculator calculator;

  @Before
  public void setUp() throws Exception {
    calculator = new Calculator();
  }

  @Test
  public void testAdd() {
    assertEquals(8, calculator.add(3,5));
  }

  @Test
  public void testMultiply() {
    assertEquals(10, calculator.multiply(2,5));
  }
}


