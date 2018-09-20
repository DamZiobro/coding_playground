/*************************************************************************************//**
 *  @file       Player.h
 *
 *  @brief      Brief description of Player.h
 *
 *  @date       2018-09-20 16:03
 *         
 **************************************************************************************/


#ifndef PLAYER_H
#define PLAYER_H

/******************************************************************//**
 *   @class    Player
 *
 *   @brief    brief description of class Player
 *********************************************************************/
#include <string>

using namespace std;

class Player {

  protected:
    int points;
    std::string name;

  public:
    Player() = delete;
    Player (const std::string& name); ///<Default constructor of class Player
    virtual ~Player (); ///<Destructor of class Player

    void setPoints(const int points) { this->points = points; }
    int getPoints() const { return this->points; }

    void setName(const std::string& name) { this->name = name; }
    std::string& getName() { return this->name; }

  private:

};

#endif /* !PLAYER_H */

