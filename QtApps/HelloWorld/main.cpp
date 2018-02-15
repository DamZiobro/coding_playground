#include <QPushButton>
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication application(argc, argv);
    QPushButton* button = new QPushButton("Hello world");
    QObject::connect(button,SIGNAL(clicked()), &application, SLOT(quit()));
    button->show();
    
    return application.exec();
    delete button;
}
