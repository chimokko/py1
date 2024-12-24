## Лаба 6 ૮ ˶ᵔ ᵕ ᵔ˶ ა
### Вариант 11 - Почтовые отправления - Расчёт цены в зависимости от расстояния, сроков, веса, объёма и типа доставки.

1. создаем папку mailing, в которой будут храниться модули letter, parcel, package с функциями calculate_price, и __init
2. в main.py импортируем tkinter, docx, openpyxl И наш пакет mailing
3. определяем функцию calculate для расчета стоимости: через .get() получаем данные из entry, определяем, какого типа посылка и применяем соответствующий модуль
4. сохраняем результат в label_res и в last_res
5. определяем функцию save
6. определяем возможные типы сохранения данных
7. в зависимости от выбранного типа данных создаем файл
8. прописываем root, создаем объекты label и button, размещаем их через .grid по сетке
9. запускаем root.mainloop()
10. вывод:

![image](https://github.com/user-attachments/assets/6fe1d0cf-d85d-4114-b70f-5c6804ad1a9d)
![image](https://github.com/user-attachments/assets/a6c8ced5-c365-4ab3-bfff-5c62a8f29e7c)
![image](https://github.com/user-attachments/assets/6b8d83fb-8e81-4777-8373-f68579f51fa2)
![image](https://github.com/user-attachments/assets/7eab6976-d2aa-4f1c-9042-047d00d65b07)

# источники:
https://docs.python.org/3/library/tkinter.html
https://python-docx.readthedocs.io/en/latest/
https://openpyxl.readthedocs.io/en/stable/
https://packaging.python.org/en/latest/tutorials/packaging-projects/
