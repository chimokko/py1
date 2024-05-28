## Лаба 5 ૮ ˶ᵔ ᵕ ᵔ˶ ა
### Вариант 9 - попискельный генератор для растровых изображений, инвертирование цветов
1. импортируем библиотеки pillow (для работы с изображениями) и functools
2. создаем функцию invert: она принимает кортеж цветов пикселя, и меняет значения цветовых каналов на противоположные
3. создаем функцию pixel_generator - генератор, который возвращает каждый пиксель из входного изображения
4. создаем функцию process_image
   
4.1. открываем изображение через Image.open(input_path) as img
   
4.2. инвертируем все пиксели изображения через map(invert, pixel_generator(img))

4.3. обозначаем размер изображения и создаем его через Image.new("RGB", (width, height))

4.4. через вложенный цикл заполняем пиксели инвертированного изображения при помощи метода putpixel

4.5. сохраняем изображение

5. вводим имя входного изображения, обозначаем файл для сохранения инвертированного изображения, запускаем process_image
6. результат работы программы:

начальное изображение "boka + yamaoka.jpg"):

![image](https://github.com/chimokko/py1/blob/main/lab5/boka%20%2B%20yamaoka.jpg)

обработанное изображение ("output_image.png"):

![image](https://github.com/chimokko/py1/blob/main/lab5/output_image.png)

## Источники:
https://pillow.readthedocs.io/en/stable/
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/functools.html
https://www.geeksforgeeks.org/python-pil-getpixel-method/
