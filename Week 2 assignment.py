# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 11:03:48 2022

@author: Saubhik
"""

#%%
def intreverse(n):
    n_str=str(n)
    n_rev=int(n_str[::-1])
    return n_rev

print(intreverse('987'))

#%%
def matched(s):
    if "(" and ")" not in s:
        return True
    if (s.count('(')!= s.count(')')):
        return(False)
    else:
        forward, reverse=0,0
        for num, i in enumerate(s):
            if i==')' and (forward)==0:
                return(False)
                break
            elif i=='(':
                forward+=1
            elif i==')':
                reverse-=1
                if len(forward)==len(reverse):
                    forward, reverse=0,0
                    if num==len(s)-1:
                        return True 


print(matched("15ababa.agaga[][[["))

#%%
def sumprimes(l):
    primes=[]
    for num in l:
        if num==2: primes.append(2)
    for i in l:
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
                elif j==i-1: primes.append(i)
    return sum(primes)

print(sumprimes([2,4,5,6,7,7,-3,1]))
