#!/usr/bin/python3
numeros = [3,5,2,6,8,9,1002,3041,782]
# lista = []
# for x in numeros:
#     if x % 2 == 0:
#         lista.append(x)
# print(lista)
par = [x for x in numeros if x % 2 == 0]
print(par)