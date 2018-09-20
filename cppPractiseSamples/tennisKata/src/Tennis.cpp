/*
 * =====================================================================================
 *       Filename:  Tennis.cpp
 *        Created:  2014-06-26 22:52
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 * =====================================================================================
 */

#include "Tennis.h"

const string Tennis::POINT_NAMES[4] = {"love", "fifteen", "thirty", "fourty"};

/* ======= Function ==================================================
 *   Name: Tennis::Tennis
 *   Description: Default contructor of class Tennis 
 * =================================================================== 
 */
Tennis::Tennis(shared_ptr<Player>& player1, shared_ptr<Player>& player2)
{
    this->player1 = player1;
    this->player2 = player2;
}

/* ======= Function ==================================================
 *   Name: Tennis::~Tennis
 *   Description: Destructor of class Tennis
 * =================================================================== 
 */
Tennis::~Tennis()
{
    //TODO
}

unique_ptr<string> Tennis::sayResult() {

    unique_ptr<string> result(new string(""));

    int pts1 = player1->getPoints();
    int pts2 = player2->getPoints();

    if (pts1 >= 3 && pts2 >= 3){
      //advantage case
      if (pts1 == pts2 +1)  {
        *result = "advantage " + player1->getName();
      } else if (pts2 == pts1 + 1) {
        *result = "advantage " + player2->getName();
      } else if(pts1 == pts2) {
        *result = "deuce";
      } else {
        if (pts1 > pts2) {
          *result = "Won " + player1->getName();
        } else {
          *result = "Won " + player2->getName();
        }
      }
    } else {
      *result = POINT_NAMES[player1->getPoints()] + " " + \
               POINT_NAMES[player2->getPoints()];
    }

    return result;
}

