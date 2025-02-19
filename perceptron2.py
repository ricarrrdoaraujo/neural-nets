#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:14:46 2019

@author: ricardo.araujo
"""

import numpy as np

entradas = np.array([-1,7,5])
pesos = np.array([0.8, 0.1, 0])

def soma(e, p):
    return e.dot(p)
#dot product / produto escalar

s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)
