from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal
from processor_class import PDFImageProcessor  # Make sure to import the model if needed

class Presenter(QObject):
    message_signal = pyqtSignal(str)  # Move this line to the class level

    def __init__(self, model):
        super().__init__()
        self.model = model

        # Connect model signals to the presenter
        self.model.message_signal.connect(self.on_message)

    @pyqtSlot()
    def select_pdf_file(self):
        self.model.select_pdf_file()

    @pyqtSlot()
    def process_pdf(self):
        self.model.process_pdf()

    def on_message(self, message):
        # Emit the message to the view through the presenter
        self.message_signal.emit(message)
