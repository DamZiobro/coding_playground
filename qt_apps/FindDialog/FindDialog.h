#ifndef _FIND_DIALOG_H
#define _FIND_DIALOG_H

#include <QDialog>

class QCheckBox;
class QLabel;
class QLineEdit;
class QPushButton;

class FindDialog : public QDialog{
    Q_OBJECT //this is necessery for all classes that defines signals or slots
public:
    FindDialog (QWidget * parent = 0);
    virtual ~FindDialog ();

signals:
    void findNext(const QString & str, Qt::CaseSensitivity cs);
    void findPrevious(const QString & str, Qt::CaseSensitivity cs);

private slots: 
    void findClicked();
    void enableFindButton(const QString &text);

private:
    QLabel *label;
    QLineEdit *lineEdit;
    QCheckBox *caseCheckBox;
    QCheckBox *backwardCheckBox;
    QPushButton *findButton;
    QPushButton *closeButton;
 
    /* data */
};

#endif //_FIND_DIALOG_H
