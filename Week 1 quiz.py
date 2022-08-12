# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:05:00 2022

@author: Saubhik
"""
#%%
#What does h(27993) return for the following function definition?

def h(x):
    (d,n) = (1,0)
    while d <= x:
        (d,n) = (d*3,n+1)
    return(n)

print(h(27933))
#%%
#What is g(60) - g(48), given the definition of g below?

def g(n): 
    s=0
    for i in range(2,n):
        if n%i == 0:
           s = s+1
    return(s)
print(g(60) - g(48))
#%%
#Consider the following function f.

def f(n): 
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           s = 1
    return(s%2 == 1)

#n/i=i
#i*i=i^2=n
#i=n^(1/2)
#since i is a natural number, n^(1/2) must be a natural number. So n has to be a perfect square number

print(f(6))
'''
The function f(n) given above returns True for a positive number n if and only if:

 n is an odd number.
 n is a prime number.
 n is a perfect square.
 n is a composite number
'''
#%%
#Consider the following function foo.

def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))

'''  
Which of the following is correct?

 The function always terminates with foo(n) = factorial of n
 The function always terminates with foo(n) = n(n+1)/2
 The function terminates for non­negative n with foo(n) = factorial of n
 The function terminates for non­negative n with foo(n) = n(n+1)/2
'''
print(foo(5))

'''
# 1st m=5, 5+mys(5-1)
# 2nd m=4, 4+mys(4-1)
# 3rd m=3, 3+mys(3-1)
....
# n-1th m=2, 2+mys(2-1)
# n th  m=1, 1+mys(1-1)=1+0=1

'''

