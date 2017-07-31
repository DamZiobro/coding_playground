/*
 * =====================================================================================
 *
 *       Filename:  FindDialog.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  13/11/13 20:55:43
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Damian Ziobro        (ziobro.damian@gmail.com)
 *        Company:  XMementoIT Limited       (info@xmementoit.com)
 *
 * =====================================================================================
 */

#include "FindDialog.h"
#include <QtGui>
#include <QCheckBox>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>


FindDialog::~FindDialog(){
    delete label;
    label = NULL;

    delete lineEdit;
    lineEdit = NULL;

    delete caseCheckBox;
    caseCheckBox = NULL;

    delete findButton;
    findButton = NULL;

    delete closeButton;
    closeButton = NULL;
}

FindDialog::FindDialog(QWidget * parent) : QDialog(parent){
    label = new QLabel(tr("Find &what:"));
    lineEdit = new QLineEdit();
    label->setBuddy(lineEdit);

    caseCheckBox = new QCheckBox(tr("Match &case"));
    backwardCheckBox = new QCheckBox(tr("Search &backward"));

    findButton = new QPushButton(tr("&Find"));
    findButton->setDefault(true);
    findButton->setEnabled(false);

    closeButton = new QPushButton(tr("Close"));

    connect(lineEdit, SIGNAL(textChanged(const QString&)), this, SLOT(enableFindButton(const QString &)));
    connect(findButton, SIGNAL(clicked()), this, SLOT(findClicked()));
    connect(closeButton, SIGNAL(clicked()), this, SLOT(close()));

    ///create layout 
    QHBoxLayout *topLeftLayout = new QHBoxLayout();
    topLeftLayout->addWidget(label);
    topLeftLayout->addWidget(lineEdit);

    QVBoxLayout *leftLayout = new QVBoxLayout();
    leftLayout->addLayout(topLeftLayout);
    leftLayout->addWidget(caseCheckBox);
    leftLayout->addWidget(backwardCheckBox);

    QVBoxLayout *rightLayout = new QVBoxLayout();
    rightLayout->addWidget(findButton);
    rightLayout->addWidget(closeButton);
    rightLayout->addStretch();

    QHBoxLayout *mainLayout = new QHBoxLayout();
    mainLayout->addLayout(leftLayout);
    mainLayout->addLayout(rightLayout);
    setLayout(mainLayout);

    setWindowTitle(tr("Find"));
    setFixedHeight(sizeHint().height());
}

void FindDialog::findClicked(){
    QString text = lineEdit->text();
    Qt::CaseSensitivity cs = caseCheckBox->isChecked() ? Qt::CaseSensitive : Qt::CaseInsensitive;

    if(backwardCheckBox->isChecked()){
        emit findPrevious(text, cs);
    } else {
        emit findNext(text, cs);
    }
}

void FindDialog::enableFindButton(const QString & text){
    findButton->setEnabled(!text.isEmpty());
}


