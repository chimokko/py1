#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'fight club, no country for old men, your name, oldboy, gruz 200'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

movies = []
a = ''
i=0
while i<len(my_favorite_movies):
    if i<len(my_favorite_movies)-1 and my_favorite_movies[i] == ',' and my_favorite_movies[i+1] == ' ':
        movies.append(a)
        a=''
        i+=2
    elif i==len(my_favorite_movies)-1:
        a+=my_favorite_movies[i]
        movies.append(a)
        i+=1
    else:
        a+=my_favorite_movies[i]
        i+=1

print(movies)
print(movies[0])
print(movies[-1])
print(movies[1])
print(movies[-2])
