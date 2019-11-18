# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:50:16 2019

@author: Chirag
"""

import hello

def test_min():
    values = (2, 3, 1, 4, 6)

    val = hello.min(values)
    assert val == 1
    
def test_max():
    values = (1,2,3,4,5,6)
    
    val = hello.max(values)
    assert val == 6
