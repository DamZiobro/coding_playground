/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  first user interaction in QT application
 *
 *        Version:  1.0
 *        Created:  13/11/13 20:04:59
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 *
 * =====================================================================================
 */

#include <QApplication>
#include <QHBoxLayout>
#include <QSlider>
#include <QSpinBox>

/* ======= Function ==================================================
 *   Name: main
 *   Description: main entry Function
 * =================================================================== 
 */
int main(int argc, const char *argv[])
{
    QApplication app(argc, (char**)argv);

    QWidget * window = new QWidget();
    window->setWindowTitle("Enter your age");

    QSpinBox * spinBox = new QSpinBox();
    QSlider* slider = new QSlider(Qt::Horizontal);
    spinBox->setRange(0,130);
    slider->setRange(0,130);

    //connect signals to intaractivly change values between slider and spinbox
    QObject::connect(spinBox, SIGNAL(valueChanged(int)), slider, SLOT(setValue(int)));
    QObject::connect(slider, SIGNAL(valueChanged(int)), spinBox, SLOT(setValue(int)));

    spinBox->setValue(35);

    //create layout
    QHBoxLayout *layout = new QHBoxLayout();
    layout->addWidget(spinBox);
    layout->addWidget(slider);
    window->setLayout(layout);

    window->show();

    return app.exec();
}
