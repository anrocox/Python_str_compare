#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: anroco

In python how to check whether two strings are equal?

En python ¿como verificar si dos strings son iguales?
'''

#create two str
s1 = 'hello world'
s2 = 'hello world'
print(s1)

#uses the == operator to determine if the values ​​of the two strings are equal
print(s1 == s2)

#create a str from the join of several strings contained in a list
s3 = ' '.join(['hello', 'world'])

#compares the values ​​of the strings s1 and s3. Return True.
print(s1 == s3)

#compares the string object references.
print(s1 is s2)
print(s1 is s3)
