/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  13/11/13 20:49:15
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 *
 * =====================================================================================
 */

#include <QApplication>
#include <FindDialog.h>

/* ======= Function ==================================================
 *   Name: main
 *   Description: main entry Function
 * =================================================================== 
 */
int main(int argc, const char *argv[])
{
    QApplication app(argc, (char**)argv);
    FindDialog *dialog = new FindDialog();
    dialog->show();
    return app.exec();
}

