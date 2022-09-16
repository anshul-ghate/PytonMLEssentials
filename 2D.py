# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:22:28 2022

@author: Anshul
"""
row = int(input("No. rows: "))
col = int(input("No. columns: "))
mult = [[0 for col in range(col)] for row in range(row)]

for row in range(row):
    for col in range(col):
        mult[row][col] = row*col
        
print(mult)
