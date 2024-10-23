# PageDivider

**Описание**:  
PageDivider — это приложение на Python, использующее библиотеку PyQt6 для создания графического интерфейса. Программа позволяет пользователям выбирать PDF-файлы, удалять гиперссылки и извлекать страницы в формате PNG. Извлеченные изображения могут быть дополнительно разделены на части для удобства использования.

**Основные функции**:
- Выбор PDF-файла через диалоговое окно.
- Удаление гиперссылок из PDF-документа.
- Сохранение страниц PDF в формате PNG.
- Разделение изображений на части с возможностью настройки ширины и максимального остатка.
- Отображение сообщений о ходе выполнения операций в интерфейсе.

**Технологии**:
- Python
- PyQt6
- PyMuPDF (fitz)
- Pillow (PIL)

**Установка**:
1. Клонируйте репозиторий:
   ```bash
   git clone <URL_репозитория>
   ```
2. Установите необходимые зависимости:
   ```bash
   pip install PyQt6 PyMuPDF Pillow
   ```
3. Запустите приложение:
   ```bash
   python main.py
   ```

**Лицензия**:  
Этот проект лицензирован под MIT License.