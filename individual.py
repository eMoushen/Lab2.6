#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    products = []
    while True:
        print("Напишите Help для справк по программе")
        print("введите комаду")
        command = input()

        if command == "Help" or command == "help" or command == "HELP":
            print("Список команд:\n")
            print("[add - добавить товар]")
            print("[list - вывести список товаров]")
            print("[select - товары в наличии]")
            print("[help - отобразить справку]")
            print("[exit - завершить работу с программой]")

        elif command == "add":
            print("сколько добавить товаров?")
            kol = int(input())
            k = 0
            for m in range(kol):
                k = k + 1
                name = input("Введите название для "+"{}".format(k)+" товара:  ")
                shope = input("Введите название магазина:  ")
                price = int(input("Стоимость товара:  "))
                product = {
                    'name': name,
                    'price': price,
                    'shope': shope,
                }
                products.append(product)
                products.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 5,
                '-' * 20,
                '-' * 14,
                '-' * 17
            )
            print(line)
            print(
                '| {:^5} | {:^20} | {:^14} | {:^17} |'.format(
                    "№",
                    "Название товара",
                    "Цена",
                    "Название магазина"
                )
            )
            print(line)
            # Вывести данные о всех товарах.
            for idx, product in enumerate(products, 1):
                print(
                    '| {:>5} | {:<20} | {:<14} | {:>17} |'.format(
                        idx,
                        product.get('name', ''),
                        product.get('price', 0),
                        product.get('shope', '')
                    )
                )
            print(line)

        elif command == 'exit':
            break

        elif command == 'select':
            # Проверить наличие товара.
            nalich = "new balance"

            flag = False
            for product in products:
                if nalich in product['name']:
                    print(f'Товар в наличии: {product["name"]}\nЦена: {product["price"]}\n')
                    flag = True

            if not flag:
                print(f'\nТаких товаров нет: {nalich}')
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)