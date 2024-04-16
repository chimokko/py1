#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
species = []
species.extend(garden_set)
species.extend(meadow_set)
species = set(species)
print(f'flower spiecies: {species}')

# выведите на консоль те, которые растут и там и там
both = []
for i in species:
    if i in garden_set and i in meadow_set:
        both.append(i)
print(f'both in garden and meadow: {both}')

# выведите на консоль те, которые растут в саду, но не растут на лугу
garden_only = []
for i in species:
    if i in garden_set and i not in meadow_set:
        garden_only.append(i)
print(f'only in garden: {garden_only}')

# выведите на консоль те, которые растут на лугу, но не растут в саду
meadow_only = []
for i in species:
    if i not in garden_set and i in meadow_set:
        meadow_only.append(i)
print(f'only in meadow: {meadow_only}')
