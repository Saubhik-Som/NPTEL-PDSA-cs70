# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:05:24 2022

@author: Saubhik
"""

#%%
"""
Define a Python function remdup(l) that takes a nonempty list of 
integers l and removes all duplicates in l, keeping only the first 
occurrence of each number.
"""
def remdup(l):
    l_new=[]
    for i in l:
        if i not in l_new:
            l_new.append(i)
    return l_new

l=['a','c',33,'a','u',33,33,33]
print(remdup(l))
#%%
def remdup_short(l):
    return list(set(l))

print(remdup_short(l))
#%%
"""
Write a Python function sumsquare(l) that takes a nonempty list of 
integers and returns a list [odd,even], where odd is the sum of squares 
all the odd numbers in l and even is the sum of squares of all the even 
numbers in l.
"""
def sumsquare(l):
    odd_sq=[]
    even_sq=[]
    for i in l:
        if i%2==0:
            even_sq.append(i**2)
        else: odd_sq.append(i**2)
    return [sum(odd_sq), sum(even_sq)]

print(sumsquare([1,2,3,4,5,6]))
print(sumsquare([1,4,9,16,25,36,49,64]))
print(sumsquare([0,1,-1,3,-3]))
#%%
'''
A two dimensional matrix can be represented in Python row-wise, 
as a list of lists: each inner list represents one row of the matrix. 
For instance, the matrix

1  2  3  4
5  6  7  8
would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].

The transpose of a matrix converts each row into a column. The 
transpose of the matrix above is:

1  5
2  6
3  7
4  8
which would be represented as [[1, 5], [2, 6], [3, 7], [4, 8]].

Write a Python function transpose(m) that takes as input a two 
dimensional matrix m and returns the transpose of m. 
The argument m should remain undisturbed by the function.
'''
#(3,2)-->>(2,3)
def transpose(m):
    transp_m=[]
    temp=[]
    for row in range(len(m)):
        temp.append(0)
    for column in range(len(m[row])):
        transp_m.append(temp[:])
    
    for row in range(len(m)):
        for column in range(len(m[row])):
            transp_m[column][row]=m[row][column]
    return transp_m

m=[[1, 2, 3, 4], [5, 6, 7, 8]]
print(transpose(m))

#%%
import numpy as np
def transpose_np (m):
    m=np.array(m)
    m_transp=m.transpose()
    return m_transp
m=[[1, 2, 3, 4], [5, 6, 7, 8]]
print(transpose_np(m))

































