#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["dad","mom","bro"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['gendo', 180],
    ['yui',170],
    ['silly',165]
]

# Выведите на консоль рост отца в формате
print(f"dad's height: {my_family_height[0][1]}")

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
sh = 0
for i in range(len(my_family_height)):
    sh += my_family_height[i][1]
print(f"summed family height: {sh}")
