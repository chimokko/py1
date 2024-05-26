## Замыкание для записи всех значений в файл
1. создаем функцию create_writer, в которую передаем файл для записи
2. прописываем открытие файла
3. создаем функцию writer, которая открывает файл и записывает в него значение
4. f.flush() - эта строка позволит записать данные в файл во время работы программы, не храня их в буфере операционки
5. вызываем функцию create_writer
6. записываем значения при помощи функции write_to_file
7. выводим значения, записанные в файл:

![image](https://github.com/chimokko/py1/assets/155952073/ad26df90-7134-4c2a-b9d4-3ff491ed8b95)

## Декоратор для асинхронного выполнения функции
1. импортируем библиотеку asymcio
2. создаем функцию async_decorator и в ней функцию wrapper, в которую обернем декорируемую функцию
3. в wrapper получаем действующий цикл событий через asyncio.get_running_loop(), возвращаем цикл, выполняющийся в потоке
4. создаем функцию из предыдущего задания с асинхронным декоратором
5. создаем асинхронную функцию main
6. в main вызываем await create_writer
7. записываем значения при помощи writer
8. выводим записанные в файл значения (файл не был форматирован после исполнения предыдущей проги):
![image](https://github.com/chimokko/py1/assets/155952073/8ea34703-bfd7-4f2e-8162-da655163c374)

## Источники:
https://docs.python.org/3/tutorial/inputoutput.html
https://www.programiz.com/python-programming/closure
https://stackoverflow.com/questions/7127075/what-exactly-is-file-flush-doing
https://docs.python.org/3/library/asyncio.html
https://docs.python.org/3/library/asyncio-eventloop.html
