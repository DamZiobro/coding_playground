/*
 * =====================================================================================
 *       Filename:  mainwindow.h
 *    Description:  
 *        Created:  2014-02-01 18:31
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 * =====================================================================================
 */


#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QDeclarativeView>

class MainWindow : public QDeclarativeView
{
    Q_OBJECT

    public:
        MainWindow(QWidget *parent = 0);
        ~MainWindow();
};

#endif /* !MAINWINDOW_H */

