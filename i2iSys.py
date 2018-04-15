#!/usr/bin/python
#-*-coding:utf-8-*-

def cift(dizi, deger):
    return [i for i, x in enumerate(dizi) if x == deger]

def fn(alt_dizi):
    try:
        for i in cift(dizi, alt_dizi[0]):
            if alt_dizi == dizi[i: i + len(alt_dizi)]:
             return "Var"
    except ValueError:
        return "Yok"
    return "Yok"





   

