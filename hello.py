# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def max(values):

  _max = values[0]

  for val in values:
      if val > _max:
          _max = val

  return _max

def min(values):
    _min = values[0]
    
    for val in values:
        if val < _min:
            _min=val
            
    return _min

#print("Hi")
