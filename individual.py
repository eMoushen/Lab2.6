#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    list_of_dicts = list()

    for i in range(3):
        my_dict = dict()

        my_dict['Название товара'] = input("Введите название товара: ")
        my_dict['Название магазина'] = input("Введите название магазина: ")
        my_dict['Стоимость товаров в руб'] = int(input("Введите стоимость: "))

        list_of_dicts.append(my_dict)

    list_of_dicts = sorted(list_of_dicts, key=lambda x: x["Название товара"])
    is_find = False

    for item in list_of_dicts:
        if item['Название товара'].__contains__('New balance'):
            print(f'\nТовар в наличии: {item["Название товара"]}\nЦена: {item["Стоимость товаров в руб"]}\n\n')
            is_find = True

    if not is_find:
        print("Таких товаров нет!")