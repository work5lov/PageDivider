import os
from PIL import Image
import fitz  # PyMuPDF
from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt6.QtWidgets import QFileDialog
import re

class PDFImageProcessor(QObject):
    # Сигнал для вывода сообщений на интерфейс
    message_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.pdf_path = ""

    @pyqtSlot()
    def select_pdf_file(self):
        # Отображаем диалог выбора файла
        file_name, _ = QFileDialog.getOpenFileName(None, "Выберите PDF файл", "", "PDF Files (*.pdf);;All Files (*)")
        if file_name:
            file_name_only = os.path.basename(file_name)  # Получаем только имя файла
            self.pdf_path = file_name
            self.message_signal.emit(f"Файл выбран: {file_name_only}")
        else:
            self.message_signal.emit("Файл не выбран.")

    # Запуск обработки PDF и изображений
    @pyqtSlot()
    def process_pdf(self):
        if not os.path.exists(self.pdf_path):
            self.message_signal.emit("Файл не существует!")
            return

        self.message_signal.emit("Начинается обработка PDF...")

        # Удаляем гиперссылки и сохраняем страницы как PNG
        self.remove_hyperlinks_and_save_as_png(self.pdf_path)

        # Теперь обрабатываем каждую сохраненную PNG
        image_names = [f"{self.pdf_path[:-4]}_{i + 1}.png" for i in range(3)]  # Можно динамически получить количество страниц
        output_folder = os.path.dirname(self.pdf_path)
        for image_name in image_names:
            self.split_images(image_name, output_folder)

        self.message_signal.emit("Обработка завершена.")

    def remove_hyperlinks_and_save_as_png(self, pdf_path):
        doc = fitz.open(pdf_path)
        base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
        output_folder = os.path.dirname(pdf_path)

        for page_number in range(len(doc)):
            page = doc[page_number]
            links = page.get_links()
            for link in links:
                page.delete_link(link)

            png_filename = os.path.join(output_folder, f"{base_filename}_{page_number + 1}.png")
            pix = page.get_pixmap()
            pix.save(png_filename)
            self.message_signal.emit(f"Сохранена {png_filename}")

        doc.saveIncr()
        doc.close()

    def sanitize_filename(self, filename):
        # Заменяем недопустимые символы на "_"
        return re.sub(r'[<>:"/\\|?*]', '_', filename)

    def split_images(self, image_name, output_folder, target_width_mm=297, max_remainder_mm=100):
        # Создаем директорию для сохранения частей, если её нет
        parts_folder = os.path.join(output_folder, "страницы по частям")
        os.makedirs(parts_folder, exist_ok=True)

        img = Image.open(image_name)
        img_width, img_height = img.size

        dpi = 72  # Делаем фиксированное значение DPI
        target_width_px = int((target_width_mm / 25.4) * dpi)
        num_parts = img_width // target_width_px
        remainder = img_width % target_width_px

        if remainder > 0 and remainder < int((max_remainder_mm / 25.4) * dpi):
            target_width_px = (img_width - remainder) // num_parts if num_parts > 0 else img_width
            num_parts = img_width // target_width_px

        part_number = 0
        for part in range(num_parts):
            left = part * target_width_px
            right = min(left + target_width_px, img_width)
            img_part = img.crop((left, 0, right, img_height))

            # Генерируем безопасное имя файла
            sanitized_image_name = self.sanitize_filename(os.path.basename(image_name))
            img_part.save(os.path.join(parts_folder, f"{sanitized_image_name}_part_{part_number}.png"))
            part_number += 1

        self.message_signal.emit(f"{image_name} разделено на {num_parts} частей.")