# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:18:31 2018

@author: Arman
"""

from sympy import *


def integral(func,upper,lower):
    x = Symbol('x')
    i = Integral(func,(x,upper,lower)).doit()
    plot(i,2,4)
    pprint(i)

if __name__=='__main__':
    func = input("Enter the function: ")
    plot(func)
    upperlimit = input("Upper Limit:")
    lowerlimit = input("Lower Limit:")
    
    integral(func,upperlimit,lowerlimit)