/*
 * =====================================================================================
 *       Filename:  qWidgets.cpp
 *    Description:  
 *        Created:  2014-02-05 01:09
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 * =====================================================================================
 */

#include "qWidgets.h"

#include <qdeclarative.h>
#include <QDeclarativeView>
#include <QApplication>
#include <QtOpenGL/QGLWidget>
#include <QPainter>
 
 
MDE::MDE(QDeclarativeItem *parent )
{
     setFlag(QGraphicsItem::ItemHasNoContents, false);
}
 
void MDE::paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget)
{
    painter->beginNativePainting();
    glBegin(GL_QUADS);
    glColor3ub(0,0,255);
    glVertex2d(0, 0);
    glVertex2d(0, height());
    glColor3ub(255,0,0);
    glVertex2d(width(), height());
    glVertex2d(width(), 0);
    glEnd();
    painter->endNativePainting();

}
 
 
int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    qmlRegisterType<MDE>("MDEPlugins", 1, 0, "MDE");

    QDeclarativeView view;
    QGLWidget *glWidget = new QGLWidget;
    view.setViewport(glWidget);
    view.setSource(QUrl::fromLocalFile("test.qml"));
    view.show();
    return app.exec();
}

