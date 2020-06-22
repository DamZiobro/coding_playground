/*
 * =====================================================================================
 *       Filename:  qWidgets.h
 *    Description:  
 *        Created:  2014-02-05 01:09
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 * =====================================================================================
 */


#ifndef QWIDGETS_H
#define QWIDGETS_H

#include <QDeclarativeItem>
 
class MDE : public QDeclarativeItem
{
     Q_OBJECT
          
    public:
          MDE(QDeclarativeItem *parent = 0);
           void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget = 0);
};
 
#endif /* !QWIDGETS_H */

