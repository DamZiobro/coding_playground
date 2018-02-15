/*
 * =====================================================================================
 *       Filename:  mainwindow.cpp
 *    Description:  
 *        Created:  2014-02-01 18:32
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 * =====================================================================================
 */

#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QDeclarativeView(parent)
{
    // transparent background
    setAttribute(Qt::WA_TranslucentBackground);
    setStyleSheet("background:transparent;");

    // no window decorations
    setWindowFlags(Qt::FramelessWindowHint);

    // set QML file
    setSource(QUrl("main.qml"));
}

MainWindow::~MainWindow()
{
}

