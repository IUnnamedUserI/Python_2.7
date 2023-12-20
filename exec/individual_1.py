#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    string = list(input("Введите строку: "))
    u = {"а", "у", "о", "ы", "э", "я", "ю", "ё", "и", "е"}
    x = set(u.intersection(string))
    print(f"Используемые гласные в строке: {x}")
    print(f"Количество гласных: {len(x)}")
    