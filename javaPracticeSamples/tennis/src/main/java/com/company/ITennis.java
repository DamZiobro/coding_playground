/*
 * ITennis.java
 * Copyright (C) 2018 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */
package com.company;

import com.company.IPlayer;
import java.lang.IllegalArgumentException;

public interface ITennis
{
  public void setPlayers(IPlayer p1, IPlayer p2) throws IllegalArgumentException;
  public String getResult();
}


