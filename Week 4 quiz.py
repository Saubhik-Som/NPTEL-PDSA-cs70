# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 00:45:19 2022

@author: Saubhik
"""
#%%
'''
Write a Python function frequency(l) that takes as input a list of integers 
and returns a pair of the form (minfreqlist,maxfreqlist) where

    minfreqlist is a list of numbers with minimum frequency in l, sorted in 
    ascending order
    
    maxfreqlist is a list of numbers with maximum frequency in l, sorted in 
    ascending order
'''
def frequency(l):
    l=sorted(l)
    l_merged=[]
    same=[]
    for num, i in enumerate(l):
        if i in same or same==[]:
            same.append(i)
            if num==len(l)-1:
                l_merged.append(same)
        else:
            l_merged.append(same)
            same=[]
            same.append(i)
    max_num=[j[0] for j in l_merged if len(j)==len(max(l_merged, key=len))]
    min_num=[j[0] for j in l_merged if len(j)==len(min(l_merged, key=len))]
    return (sorted(min_num),sorted(max_num))
    
x=frequency([1])
#%%
"""
An airline has assigned each city that it serves a unique numeric code. It has 
collected information about all the direct flights it operates, represented 
as a list of pairs of the form (i,j), where i is the code of the starting 
city and j is the code of the destination.

It now wants to compute all pairs of cities connected by one intermediate 
hop — city i is connected to city j by one intermediate hop if there are 
direct flights of the form (i,k) and (k,j) for some other city k. The airline 
is only interested in one hop flights between different cities — pairs of the form (i,i) are not useful.

Write a Python function onehop(l) that takes as input a list of pairs 
representing direct flights, as described above, and returns a list of all 
pairs (i,j), where i != j, such that i and j are connected by one hop. Note 
that it may already be the case that there is a direct flight from i to j. 
So long as there is an intermediate k with a flight from i to k and from k 
to j, the list returned by the function should include (i,j). The input list 
may be in any order. The pairs in the output list should be in 
lexicographic (dictionary) order. Each pair should be listed exactly once.

Here are some examples of how your function should work.

 
>>> onehop([(2,3),(1,2)])
[(1, 3)]

>>> onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)])
[(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]

>>> onehop([(1,2),(3,4),(5,6)])
[]
"""
def onehop (l):
    flights={}
    for city in l:
        if city[0] not in flights.keys():
            flights[city[0]]=[city[1]]
        else: flights[city[0]].append(city[1])
    hop=[]
    for i in flights:
        for k in flights[i]:
            if k in flights.keys():
                for j in flights[k]:
                    if j!=i and (i,j) not in hop:
                        hop.append((i,j))
    return sorted(hop)

print(onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)])==[(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)])
print(onehop([(1,2),(3,4),(5,6)])==[])
print(onehop([(1,3),(1,2),(2,3),(2,1),(3,2),(3,1)])==[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
print(onehop([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), 
              (1, 7), (1, 8), (1, 9), (2, 1), (2, 3), (2, 4), 
              (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 1), 
              (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), 
              (3, 9), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), 
              (4, 7), (4, 8), (4, 9), (5, 1), (5, 2), (5, 3), 
              (5, 4), (5, 6), (5, 7), (5, 8), (5, 9), (6, 1), 
              (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), 
              (6, 9), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), 
              (7, 6), (7, 8), (7, 9), (8, 1), (8, 2), (8, 3), 
              (8, 4), (8, 5), (8, 6), (8, 7), (8, 9), (9, 1), 
              (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)])==[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8), (5, 9), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), (6, 9), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 9), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)])
print(onehop([(1,2),(2,1),(3,4),(4,3)])==[])            




















