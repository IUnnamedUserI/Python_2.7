#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    first_string = set(list(input("Введите первую строку: ")))
    second_string = list(input("Введите вторую строку: "))
    x = first_string.intersection(second_string)
    print(f"Повторяющиеся символы: {x}")
    print(f"Количество повторяющихся символов: {len(x)}")
    