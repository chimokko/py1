# лаба 1 ꒰ᐢ. .ᐢ꒱
## Задача 0
1. distances = {} - создаем словарь расстояний;
2. цикл for i in sites создает словарь d = {} для каждого города из sites и запускает цикл for j in sites, который считает расстояние от города i до города j И помещает его в словарь;
3. выводим результат:
![image](https://github.com/chimokko/py1/assets/155952073/9ea2b5ba-f1a2-4f6a-9b3d-f345f09832fa)


## Задача 1
1. имортируем библиотеку math;
2. считаем площадь по формуле area = radius ** 2 * math.pi;
3. выводим в print(round(area,4)), округляя до 4 знаков после запятой - площадь расчитана;
4. считаем точки расстояние от центра окружности: d1 = (point_1[0] ** 2 + point_1[1] **2 ) ** 0.5;
5. сравниваем с радиусом и выводим результат сравнения: print(d1<=radius)
6. вывод:![image](https://github.com/chimokko/py1/assets/155952073/5b977824-1d1d-4058-bbfc-adcf808f6f02)


## Задача 2
1. расставляем знаки: res = 1 * 2 + 3 + 4 * 5;
2. выводим результат: print(res)
3. вывод:
4. ![image](https://github.com/chimokko/py1/assets/155952073/c7845112-8a3a-4452-9bbe-bc8f21a3d2a0)


## Задача 3
1. создаем массив для фильмов: movies = [];
2. строка a хранит текущее слово, набираемой циклом while, который разделяет слова по запятой с пробелом
3. выводим результат: print(movies[0])
print(movies[-1])
print(movies[1])
print(movies[-2])
4. вывод (код отредачил на паре):
![image](https://github.com/chimokko/py1/assets/155952073/f50580f0-29ed-4d18-8558-74b27c6add70)


## Задача 4
1. создаем массив массивов с именами и ростами членов семьи: my_family_height = [
    ['gendo', 180],
    ['yui',170],
    ['silly',165]
];
2. выводим рост отца: print(f"dad's height: {my_family_height[0][1]}");
3. при помощи цикла for в переменную sh складываем значения роста членов семьи
4. выводим результат: print(f"summed family height: {sh}")
5. вывод: : ![image](https://github.com/chimokko/py1/assets/155952073/27584523-10e8-4596-b44f-698f3479f7ff)


## Задача 5
1. сажаем медведя на первую позицию: zoo.insert(1,'bear')
print(zoo) - вывод массива;
2. добавляем птиц в конец зоопарка: zoo.extend(birds)
print(zoo) - и вновь выводим массив;
3. убираем слона: zoo.remove('elephant')
print(zoo);
4. print(f"lion's cage: {zoo.index('lion')+1}")
print(f"lark's cage: {zoo.index('lark')+1}") - выводим номера клеток зверей в человеческом виде
5. вывод: ![image](https://github.com/chimokko/py1/assets/155952073/3fdd5008-cca0-4101-b0e1-f0c863e8af36)


## Задача 6
1. суммируем длительности песен: sl = violator_songs_list[3][1]+violator_songs_list[5][1]+violator_songs_list[-1][1];
2. выводим округленный результат: print(f'three songs last for {round(sl,2)} minutes');
3. то же самое со словарем: violator_songs_dict['Sweetest Perfection']+violator_songs_dict['Policy of Truth']+violator_songs_dict['Blue Dress'];
4. print(f'another three songs last for {round(sl1)} minutes')
5. вывод: ![image](https://github.com/chimokko/py1/assets/155952073/ae89d3e9-1013-4ae3-a066-c0ed5956f976)


## Задача 7
1. при помощи срезов получаем искомую строку: msg = secret_message[0][3]+' '+secret_message[1][9:13]+' '+secret_message[2][5:15:2]+' '+secret_message[3][12:6:-1]+' '+secret_message[4][20:15:-1]
2. выводим: print(msg)
3. вывод: ![image](https://github.com/chimokko/py1/assets/155952073/59954572-c317-4711-8b71-d170cb1d1a7b)


## Задача 8
1. создаем множества цветов: garden_set = set(garden)
meadow_set = set(meadow);
2. species = [] - виды цветов
species.extend(garden_set)
species.extend(meadow_set)
species = set(species) - убираем дублирующиеся виды
print(f'flower spiecies: {species}') - выводим;
3. both = [] - массив для цветов, растущих везде
for i in species:
    if i in garden_set and i in meadow_set:
        both.append(i) - добавляем цветок, если он растет и там, и там
print(f'both in garden and meadow: {both}') - вывод;
4. ту же операцию проделываем для луга и сада, попеременно меняя in на not in
5. вывод: ![image](https://github.com/chimokko/py1/assets/155952073/8c5f3567-6139-44df-8c25-71fe7cf623e0)

## Задача 10
1. tables_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] + store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price'] - считаем суммарную стоимость столов в магазинах,
2. то же самое со стульями и диванами
3. print(f'tables - {tables_q} pc, cost - {tables_cost} rub')
print(f'sofas - {sofas_q} pc, cost - {sofas_cost} rub')
print(f'tables - {chairs_q} pc, cost - {chairs_cost} rub') - выводим результат;
4. вывод: ![image](https://github.com/chimokko/py1/assets/155952073/fdb89b4a-e3b9-4a7a-8f0c-6254e795bd80)

