/*
 * =====================================================================================
 *       Filename:  TennisTest.cpp
 *    Description:  
 *        Created:  2014-06-26 23:12
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 * =====================================================================================
 */

#include <gtest/gtest.h>
#include <memory>
#include <string>

#include <Tennis.h>
#include <Player.h>

/******************************************************************//**
 *   @class    TennisTest : public ::testing::Te
 *
 *   @brief    brief description of class TennisTest : public ::testing::Te
 *********************************************************************/
using namespace std;

class TennisTest : public ::testing::Test {

protected:
  unique_ptr<Tennis> game;
  shared_ptr<Player> player1;
  shared_ptr<Player> player2;

protected:
  TennisTest() {}; ///<Default constructor of class TennisTest : public ::testing::Te
  virtual ~TennisTest() {}; ///<Destructor of class TennisTest : public ::testing::Te

  virtual void SetUp() {
    player1 = shared_ptr<Player>(new Player(string("Player1")));
    player2 = shared_ptr<Player>(new Player(string("Player2")));
    game = unique_ptr<Tennis>(new Tennis(player1, player2));
  }
  virtual void TearDown() {}

};

TEST_F(TennisTest, testLoveFifty) {
  player1->setPoints(0);
  player2->setPoints(1);
  EXPECT_EQ(string("love fifteen"), *game->sayResult());
}

TEST_F(TennisTest, testThirtyFourty) {
  player1->setPoints(2);
  player2->setPoints(3);
  EXPECT_EQ(string("thirty fourty"), *game->sayResult());
}

TEST_F(TennisTest, testDeuce) {
  player1->setPoints(7);
  player2->setPoints(7);
  EXPECT_EQ(string("deuce"), *game->sayResult());
}

TEST_F(TennisTest, testAdvantage) {
  player1->setPoints(3);
  player2->setPoints(4);
  EXPECT_EQ(string("advantage Player2"), *game->sayResult());
}

TEST_F(TennisTest, testAdvantage2) {
  player1->setPoints(5);
  player2->setPoints(4);
  EXPECT_EQ(string("advantage Player1"), *game->sayResult());
}

TEST_F(TennisTest, testWon1) {
  player1->setPoints(5);
  player2->setPoints(3);
  EXPECT_EQ(string("Won Player1"), *game->sayResult());
}

TEST_F(TennisTest, testWon2) {
  player1->setPoints(6);
  player2->setPoints(8);
  EXPECT_EQ(string("Won Player2"), *game->sayResult());
}
