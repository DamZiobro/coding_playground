/*
 * =====================================================================================
 *       Filename:  main.cpp
 *    Description:  
 *        Created:  2014-02-01 18:35 
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 * =====================================================================================
 */

#include <QtGui/QApplication>
#include "mainwindow.h"

using namespace std;

/* ======= Function ==================================================
 *   Name: main
 *   Description: main entry Function
 * =================================================================== 
 */
int main(int argc, const char **argv)
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();    
    return 0;
}


