import QtQuick 1.0

Rectangle {
    id: root

    width: 250
    height: 250

    // completely transparent background
    color: "#00FFFFFF"

    border.color: "#F00"
    border.width: 2

    Rectangle {
        id: ball

        height: 50; width: 50
        x: 100

        color: "#990000FF"
        radius: height / 2
    }

    SequentialAnimation {
        running: true; loops: Animation.Infinite
        NumberAnimation { target: ball; property: "y"; to: root.height - ball.height; duration: 1000; easing.type: Easing.OutBounce }
        PauseAnimation { duration: 1000 }
        NumberAnimation { target: ball; property: "y"; to: 0; duration: 700 }
        PauseAnimation { duration: 1000 }
    }
}
