#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"a", "b", "g", "k", "m", "p"}
    b = {"b", "e", "f", "l", "r"}
    c = {"k", "l", "w", "x"}
    d = {"e", "j", "o", "p", "q", "u", "v"}

    ab = a.difference(b)
    cd = c.union(d)
    x = ab.intersection(cd)

    not_a = u.difference(a)
    not_b = u.difference(b)
    ab = not_a.intersection(not_b)
    y = ab.difference(cd)

    print(f"X = {x}")
    print(f"Y = {y}")
    