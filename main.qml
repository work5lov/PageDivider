import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("PDF Image Processor")

    Column {
        spacing: 20
        anchors.centerIn: parent

        Button {
            text: "Выбрать PDF"
            onClicked: presenter.select_pdf_file()
        }

        Button {
            text: "Начать обработку"
            onClicked: presenter.process_pdf()
        }

        Text {
            id: messageOutput
            text: ""
        }

        Connections {
            target: presenter

            function onMessage_signal(message) {
                messageOutput.text = message;  // Use the message parameter correctly
            }
        }
    }
}
