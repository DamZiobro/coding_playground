/*
 * PrimeFactorsTests.java
 */

import static org.junit.Assert.assertEquals;
import org.junit.Before;
import org.junit.Test;
import com.company.PrimeFactors;

import java.util.List;
import java.util.ArrayList;

public class PrimeFactorsTests
{

  private PrimeFactors primes;

  private List<Integer> createList(int... ints){
    List<Integer> list = new ArrayList<Integer>();
    for (int i : ints)  {
      list.add(i);
    }
    return list;
  }

  @Before
  public void setUp() throws Exception {
    primes = new PrimeFactors();
  }

  @Test
  public void testOne() {
    assertEquals(createList(), primes.generate(1));
  }

  @Test
  public void testTwo() {
    assertEquals(createList(2), primes.generate(2));
  }

  @Test
  public void testThree() {
    assertEquals(createList(3), primes.generate(3));
  }

  @Test
  public void testFour() {
    assertEquals(createList(2,2), primes.generate(4));
  }

  @Test
  public void testSix() {
    assertEquals(createList(2,3), primes.generate(6));
  }

  @Test
  public void testEight() {
    assertEquals(createList(2,2,2), primes.generate(8));
  }

  @Test
  public void testNine() {
    assertEquals(createList(3,3), primes.generate(9));
  }

  @Test
  public void testTwenty() {
    assertEquals(createList(2,2,5), primes.generate(20));
  }
}
