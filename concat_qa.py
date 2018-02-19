#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:07:06 2018

@author: nllerandi
"""
import re

f = open('Fios DCO Netflix 1.18 2 - Fios DCO Netflix 1.18 (4).csv', 'r') 
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
        
    if is_allowed_specific_char(tc) == False:
        print("Special characters present: " + tc)
        continue
        
    if cmp.find(tc) == -1:
        print("TC, CMP, URL do not match: " + tc) 

    if url.find(tc) == -1:
        print("TC, CMP, URL do not match: " + tc) 
                
# =============================================================================
# Done:
# ✓ No spaces or special characters in column J
# ✓ No discrepancies between TC, CMP, URL
# 
# WIP:
# ✓ Correct use of RT (not applicable)
# ✓ Landing pages work; no redirects
# ✓ Unique values in column W
# ✓ Landing pages are not dropping CMP codes
# ✓ No issues with concatenation
# =============================================================================
    