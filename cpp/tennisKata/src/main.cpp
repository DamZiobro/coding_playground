/*
 * =====================================================================================
 *       Filename:  main.cpp
 *    Description:  
 *        Created:  2014-06-26 22:51 
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 * =====================================================================================
 */

#include <iostream>
#include <memory>
#include <string>

#include <Tennis.h>
#include <Player.h>

using namespace std;

/* ======= Function ==================================================
 *   Name: main
 *   Description: main entry Function
 * =================================================================== 
 */
int main(int argc, const char **argv)
{
    shared_ptr<Player> player1(new Player(string("Roger Federer")));
    shared_ptr<Player> player2(new Player(string("Novak Djokovic")));
    unique_ptr<Tennis> tennis(new Tennis(player1, player2));

    cout << "Result: " << *tennis->sayResult() << endl;

    return 0;
}


