/*
 * Player.java
 * Copyright (C) 2018 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */
package com.company;

import com.company.IPlayer;
import java.lang.IllegalArgumentException;

public class Player implements IPlayer
{
  protected String name;
  protected int points;

	public Player(String name) {
    this.name = name;
    this.points = 0;
	}
  
  public void setPoints(int points) throws IllegalArgumentException {
    if (points < 0) {
      throw new IllegalArgumentException();
    }
    this.points = points;
  }

  public int getPoints() {
    return this.points;
  }

  public String getName() {
    return this.name;
  }
}


