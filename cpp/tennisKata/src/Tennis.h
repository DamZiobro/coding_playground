/*
 * =====================================================================================
 *       Filename:  Tennis.h
 *    Description:  
 *        Created:  2014-06-26 22:52
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 * =====================================================================================
 */


#ifndef Tennis_H
#define Tennis_H
#include <memory>
#include "Player.h"
#include <string>

using namespace std;

//=================================================================================
// Class Tennis
//=================================================================================

class Tennis {

    static const string POINT_NAMES[4];

    //-----------------------------------------------------------
    public:
        Tennis (shared_ptr<Player>& player1, shared_ptr<Player>& player2);
        virtual ~Tennis ();

        unique_ptr<string> sayResult ();
    
    //-----------------------------------------------------------
    protected:
        shared_ptr<Player> player1;
        shared_ptr<Player> player2;
        

    //-----------------------------------------------------------
        
    
    //-----------------------------------------------------------
    //Getters and setters 
};

//==================================================================================

#endif /* Tennis_H */


