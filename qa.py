#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:07:06 2018

@author: nllerandi
"""
import re
import requests

f = open('Fios URL Builder - VZ Campaign Code Creation Form Template 2.13_NOFS.csv - Fios URL Builder - VZ Campaign Code Creation Form Template 2.13_NOFS.csv (1).csv', 'r') 
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
    lp = i[19]
    lpr = str(requests.get(lp).status_code)
    uid = i[21][-4:]
    cmp = i[32]
    cmpuid = i[32][-4:]
    url = i[34]
    urluid = i[34][-12:-8]
    urlr = str(requests.get(url).status_code)
    
    print(uid)
        
    # ✓ No spaces or special characters in column J
    if is_allowed_specific_char(tc) == False:
        print("Special characters present: " + tc) 
    
    # ✓ Landing pages work
    if lpr != "200":
        print("LP Error : " + lpr + " : " + tc)
        
    if uid != cmpuid:
        print("UID and CMP-UID do not match : " + uid + " vs " + cmpuid)
        
    # ✓ No discrepancies between TC, CMP, URL    
    if cmp.find(tc) == -1:
        print("TC and CMP do not match: " + tc) 

    if url.find(tc) == -1:
        print("TC and URL do not match: " + tc)         
        
    if uid != urluid:
        print("UID and URL-UID do not match : " + uid + " vs " + urluid)  
    
    # ✓ Encoded URLs work    
    if urlr != "200":
        print("Encoded URL Error : " + urlr + " : " + tc)
        
print("Done")

      
# =============================================================================
# Done:
# ✓ No spaces or special characters in column J
# ✓ No discrepancies between TC, CMP, URL
# ✓ Landing pages work
# ✓ Encoded URLs work

# WIP:
# ✓ Correct use of RT 
# ✓ No redirects; Landing pages are not dropping CMP codes
# ✓ Unique values in column W; Value matches with all occurences in row
# ✓ Contains https
# =============================================================================
    