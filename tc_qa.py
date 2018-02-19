#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:54:48 2018

@author: nllerandi
"""
import re

f = open('Fios DCO Netflix 1.18 2 - Fios DCO Netflix 1.18 (3).csv', 'r') 
data = f.read()
rows = data.split('\n')
split_data = []
for row in rows:
    split_row = row.split(',')
    split_data.append(split_row) 
    
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

for i in split_data:
    tc = i[8]
    cmp = i[32]
    url = i[34]
    
    if is_allowed_specific_char(tc) == -1:
        print("Error with TC: " + tc) 

