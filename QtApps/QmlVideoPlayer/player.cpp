/*
   Copyright (C) 2010 Marco Ballesio <gibrovacco@gmail.com>
   Copyright (C) 2011-2012 Collabora Ltd.
     @author George Kiagiadakis <george.kiagiadakis@collabora.co.uk>

   This library is free software; you can redistribute it and/or modify
   it under the terms of the GNU Lesser General Public License as published
   by the Free Software Foundation; either version 2.1 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include "player.h"
#include <QUrl>
#include <QFileDialog>
#include <QGlib/Connect>
#include <QGlib/Error>
#include <QGst/ElementFactory>
#include <QGst/Bus>

Player::Player(QObject *parent)
    //: QObject(parent)
{
    //open default file to play
    //QString fileName = "/home/damian/Videos/samples/sintelTrailerHD.mkv";
    //setUri(QUrl::fromLocalFile(fileName).toEncoded());
}

void Player::setVideoSink(const QGst::ElementPtr & sink)
{
    m_videoSink = sink;
}

void Player::play()
{
    if (m_pipeline) {
        m_pipeline->setState(QGst::StatePlaying);
    }
}

void Player::stop()
{
    if (m_pipeline) {
        m_pipeline->setState(QGst::StateNull);
    }
}

void Player::open()
{
    // parent() is the QDeclarativeView here
    QString fileName = QFileDialog::getOpenFileName(qobject_cast<QWidget*>(parent()),
                                                    tr("Open a Movie"), m_baseDir);

    if (!fileName.isEmpty()) {
        openFile(fileName);
    }
}

void Player::openFile(const QString & fileName)
{
    m_baseDir = QFileInfo(fileName).path();

    stop();
    setUri(QUrl::fromLocalFile(fileName).toEncoded());
    play();
}

void Player::setUri(const QString & uri)
{
    if (!m_pipeline) {
        m_pipeline = QGst::ElementFactory::make("playbin2").dynamicCast<QGst::Pipeline>();
        if (m_pipeline) {
            m_pipeline->setProperty("video-sink", m_videoSink);

            //watch the bus for messages
            QGst::BusPtr bus = m_pipeline->bus();
            bus->addSignalWatch();
            QGlib::connect(bus, "message", this, &Player::onBusMessage);
        } else {
            qCritical() << "Failed to create the pipeline";
        }
    }

    if (m_pipeline) {
        m_pipeline->setProperty("uri", uri);
    }
}

void Player::onBusMessage(const QGst::MessagePtr & message)
{
    switch (message->type()) {
    case QGst::MessageEos: //End of stream. We reached the end of the file.
        stop();
        break;
    case QGst::MessageError: //Some error occurred.
        qCritical() << message.staticCast<QGst::ErrorMessage>()->error();
        stop();
        break;
    default:
        break;
    }
}

#include "moc_player.cpp"
