#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:17:06 2018

@author: nllerandi
"""

data = open('learn shop pages ES.xlsx - 2 (1).csv', 'r').read()
dataNH = data.split('\n')[2:]
variety = {}

for row in dataNH:
    if row in variety:
        variety[row] = variety[row] + 1
    else:
        variety[row] = 1

variety