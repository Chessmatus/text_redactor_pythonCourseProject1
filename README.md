# Проект Текстовый редактор

Текстовый редактор - базовый текстовый редактор.

![Интерфейс приложения](https://github.com/Chessmatus/project_01/blob/dev/screenshot.png)  

1. Возможности:
   * Открывать, редактировать, сохранять текстовые файлы.
   
![Open file](https://github.com/Chessmatus/project_01/blob/dev/screenshot_1.png) 

   * Выполнять копирование, вставку, поиск и поиск с заменой по тексту.
   
![Интерфейс приложения](https://github.com/Chessmatus/project_01/blob/dev/screenshot_2.png) 

   * Менять цвет, фон текста. Доступные цвета: белый, черный, серый, желтый, красный, синий, зеленый. Также можно менять общий фон. Доступные цвета: белый, черный.

![Интерфейс приложения](https://github.com/Chessmatus/project_01/blob/dev/screenshot_3.png) 

2. Запуск приложения:

   Выполнить в консоли:
   
   ```
   git clone https://github.com/Chessmatus/project_01.git 
   cd project_01
   git checkout -b dev origin/dev
   pip install -r requirements.txt
   python3 window.py
   
3. Замечания:
   * Использовалась библиотека PyQT5. [Ссылка на документацию](https://doc.qt.io/qtforpython/).
