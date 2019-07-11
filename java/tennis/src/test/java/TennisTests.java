/*
 * TennisTests.java
 */

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import org.junit.Before;
import org.junit.Test;
import com.company.ITennis;
import com.company.Tennis;
import com.company.IPlayer;
import com.company.Player;

import java.lang.IllegalArgumentException;

public class TennisTests
{

  private ITennis tennis;
  private IPlayer player1;
  private IPlayer player2;

  @Before
  public void setUp() {
    player1 = new Player("Roger Federer");
    player2 = new Player("Novak Djokovic");
    tennis = new Tennis(player1, player2);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testPlayersNotTheSame() {
    tennis.setPlayers(player1, player1);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testPointsNegative() {
    player1.setPoints(-1);
  }

  @Test
  public void testAdvantage() {
    player1.setPoints(4);
    player2.setPoints(3);
    
    assertTrue(tennis.getResult().equals("advantage Roger Federer"));
  }

  @Test
  public void testLoveFifteen() {
    player1.setPoints(0);
    player2.setPoints(1);
    
    assertTrue(tennis.getResult().equals("love fifteen"));
  }

  @Test
  public void testThirtyForty() {
    player1.setPoints(2);
    player2.setPoints(3);
    
    assertTrue(tennis.getResult().equals("thirty forty"));
  }

  @Test
  public void testDeuce() {
    player1.setPoints(5);
    player2.setPoints(5);
    
    assertTrue(tennis.getResult().equals("deuce"));
  }

  @Test
  public void testWonPlayer2() {
    player1.setPoints(3);
    player2.setPoints(5);
    
    assertTrue(tennis.getResult().equals("Won Novak Djokovic"));
  }

  @Test
  public void testWonPlayer1WithoutAdvantage() {
    player1.setPoints(4);
    player2.setPoints(1);
    
    assertTrue(tennis.getResult().equals("Won Roger Federer"));
  }
}
