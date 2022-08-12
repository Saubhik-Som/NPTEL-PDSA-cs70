# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 17:17:29 2022

@author: Saubhik
"""


#%%
"""
A positive integer m can be expresseed as the sum of three squares if 
it is of the form p + q + r where p, q, r ≥ 0, and p, q, r are all 
perfect squares. For instance, 2 can be written as 0+1+1 but 7 
cannot be expressed as the sum of three squares. The first numbers 
that cannot be expressed as the sum of three squares are 7, 15, 23, 
28, 31, 39, 47, 55, 60, 63, 71, … (see Legendre's three-square theorem).

Write a Python function threesquares(m) that takes an integer 
m as input and returns True if m can be expressed as the sum 
of three squares and False otherwise. (If m is not positive, 
your function should return False.)
"""
def threesquares(m):
    if m<0:
        return False
    for a in range(0,m+1):
        for b in range (0,m+1):
            n = 4**a*(8*b + 7) #from Legendre's three-square theorem
            if n==m:
                return False
    return True

print(threesquares(56))

#%%
"""
Write a function repfree(s) that takes as input a string s and 
checks whether any character appears more than once. The function 
should return True if there are no repetitions and False otherwise.
"""
def repfree(s):
    char_list=[]
    for i in s:
        if i not in char_list:
            char_list.append(i)
        else: return (False)
    return (True)

print(repfree("qwerty!@#2"))
print(repfree("(x+6)(y-5)"))
print(repfree("94templars"))
print(repfree("siruseri"))
#%%
"""
A list of numbers is said to be a hill if it consists of an ascending
 sequence followed by a descending sequence, where each of the 
 sequences is of length at least two. Similarly, a list of numbers 
 is said to be a valley if it consists of an descending sequence 
 followed by an ascending sequence. You can assume that consecutive
 numbers in the input sequence are always different from each other.

Write a Python function hillvalley(l) that takes a list l of 
integers and returns True if it is a hill or a valley, and False 
otherwise.
"""
def hillvalley(l):
    hc,vc=0,0
    for i in range(len(l)-1):
        if 0<i:
            if l[i-1]<l[i]>l[i+1]:
                hc+=1
            elif l[i-1]>l[i]<l[i+1]:
                vc+=1
    if hc==1 and vc==0:
        return (True)
    elif hc==0 and vc==1:
        return (True)
    else:
        return (False)

print(hillvalley([1,2,3,5,4,3,2,1]))
print(hillvalley([1,2,3,4,5,3,2,4,5,3,2,1]))
print(hillvalley([9,5,4,-1,-2,3,7]))
print(hillvalley([5,4,3,2,1,0,-1,-2,-3]))










