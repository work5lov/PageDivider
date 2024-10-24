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
        width: parent.width  // Убедитесь, что колонка занимает всю ширину окна

        Button {
            text: "Выбрать PDF"
            onClicked: presenter.select_pdf_file()
            anchors.horizontalCenter: parent.horizontalCenter  // Центрируем кнопку
        }

        Button {
            text: "Начать обработку"
            onClicked: presenter.process_pdf()
            anchors.horizontalCenter: parent.horizontalCenter  // Центрируем кнопку
        }

        Text {
            id: messageOutput
            text: ""
            anchors.horizontalCenter: parent.horizontalCenter  // Центрируем текст
        }

        Connections {
            target: presenter

            function onMessage_signal(message) {
                messageOutput.text = message;  // Используем параметр message правильно
            }
        }
    }
}
