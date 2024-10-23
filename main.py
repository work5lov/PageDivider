import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine
from processor_class import PDFImageProcessor
from presenter import Presenter

if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    model = PDFImageProcessor()
    presenter = Presenter(model)

    # Add presenter to QML context
    engine.rootContext().setContextProperty("presenter", presenter)

    # Load QML
    engine.load("main.qml")

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
