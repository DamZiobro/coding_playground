/*
 * Tennis.java
 * Copyright (C) 2018 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

package com.company;

import com.company.ITennis;
import java.lang.IllegalArgumentException;
import java.lang.StringBuilder;

public class Tennis implements ITennis
{
  protected IPlayer player1;
  protected IPlayer player2;

  protected String[] results = new String[]{"love", "fifteen", "thirty", "forty"};

	public Tennis(IPlayer p1, IPlayer p2) {
    this.setPlayers(p1, p2);
	}

  public void setPlayers(IPlayer p1, IPlayer p2) throws IllegalArgumentException {
    if (p1 == p2) {
      throw new IllegalArgumentException();
    }

    this.player1 = p1;
    this.player2 = p2;
  }

  public String getResult(){
    StringBuilder result = new StringBuilder("");
    int pts1 = player1.getPoints();
    int pts2 = player2.getPoints();
    
    //test whether anyone won
    if (pts1 > 3 && pts1 >= pts2+2) {
      result.append("Won " + player1.getName());
    } else if (pts2 > 3 && pts2 >= pts1+2) {
      result.append("Won " + player2.getName());
    } else if (pts1 >= 3 && pts2 >= 3) {
      //check advantage or deuce
      if (pts1 == pts2) {
        result.append("deuce");
      } else {
        result.append("advantage ");
        if (pts1 == pts2+1) {
          result.append(player1.getName());
        } else if (pts2 == pts1 +1) {
          result.append(player2.getName());
        } 
      }
    } else {
      //normal result 
      result.append(results[pts1] + " " + results[pts2]);
    }


    return result.toString();
  }

}


