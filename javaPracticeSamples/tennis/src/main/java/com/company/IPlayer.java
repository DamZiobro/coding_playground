/*
 * IPlayer.java
 * Copyright (C) 2018 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

package com.company;

import java.lang.IllegalArgumentException;

public interface IPlayer
{
  void setPoints(int points) throws IllegalArgumentException;
  int getPoints();
  String getName();
}


