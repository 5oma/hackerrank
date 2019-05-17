#!/bin/python3

import sys
import math

def lowestTriangle(base, area):
    # determinando altura
    height = (2 * area) / base
    # convirtiendo altura al siguiente int
    height_min = int(math.ceil(height))
    return height_min
