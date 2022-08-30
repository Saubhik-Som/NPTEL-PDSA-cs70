# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 00:37:11 2022

@author: Saubhik
"""
#%%
'''
We represent scores of batsmen across a sequence of matches in a two 
level dictionary as follows:

{'match1':{'player1':57, 'player2':38}, 
 'match2':{'player3':9, 'player1':42}, 
 'match3':{'player2':41, 'player4':63, 'player3':91}
Each match is identified by a string, as is each player. The scores 
are all integers. The names associated with the matches are not fixed 
(here they are 'match1', 'match2', 'match3'), nor are the names of the 
players. A player need not have a score recorded in all matches.

Define a Python function orangecap(d) that reads a dictionary d of 
this form and identifies the player with the highest total score. Your 
function should return a pair (playername,topscore) where playername 
is a string, the name of the player with the highest score, and 
topscore is an integer, the total score of playername.

The input will be such that there are never any ties for highest total 
score.
'''
def orangecap(d):
    score_dict={}
    for match in d:
        for player in d[match]:
            if player in score_dict.keys():
                score_dict[player]+=d[match][player]
            else: score_dict[player]=d[match][player]
    score_tuple=zip(score_dict.values(),score_dict.keys())
    return max(score_tuple)[::-1]
                
print(orangecap({'match1':{'player1':57, 'player2':38}, 
                 'match2':{'player3':9, 'player1':42}, 
                 'match3':{'player2':41, 'player4':63, 'player3':91}}))
#%%
'''
Let us consider polynomials in a single variable x with integer 
coefficients. For instance:

3x4 - 17x2 - 3x + 5
Each term of the polynomial can be represented as a pair of integers 
(coefficient,exponent). The polynomial itself is then a list of such 
pairs.

We have the following constraints to guarantee that each polynomial 
has a unique representation:

Terms are sorted in descending order of exponent
No term has a zero cofficient
No two terms have the same exponent
Exponents are always nonnegative
For example, the polynomial introduced earlier is represented as:

[(3,4),(-17,2),(-3,1),(5,0)]
The zero polynomial, 0, is represented as the empty list [], since it 
has no terms with nonzero coefficients.

Write Python functions for the following operations:

addpoly(p1,p2)
multpoly(p1,p2)
that add and multiply two polynomials, respectively.

You may assume that the inputs to these functions follow the 
representation given above. Correspondingly, the outputs from these 
functions should also obey the same constraints.

You can write auxiliary functions to "clean up" polynomials – e.g., 
remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that can be combined to achieve the desired format.

You may also want to convert the list representation to a dictionary 
representation and manipulate the dictionary representation, and then 
convert back.

Some examples:

  
   >>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
   [(2, 1),(3, 0)]

   Explanation: (4x^3 + 3) + (-4x^3 + 2x) = 2x + 3

   >>> addpoly([(2,1)],[(-2,1)])
   []

   Explanation: 2x + (-2x) = 0

   >>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
   [(1, 3),(-1, 0)]

   Explanation: (x - 1) * (x^2 + x + 1) = x^3 - 1
'''
def cleanup(p):
    eq={}
    for pair in p:
        coeff=pair[0]
        exp=pair[1]
        if coeff!= 0 and exp>=0:
            if exp not in eq.keys():
                eq[exp]=coeff
            else: eq[exp]+=coeff
    return eq

def addpoly(p1,p2):
    p1=cleanup(p1)
    p2=cleanup(p2)
    for key in p2:
        if key not in p1.keys():
            p1[key]=p2[key]
        else: p1[key]+=p2[key]
    addition= [(i,j) for i,j in zip(p1.values(),p1.keys()) if i!=0]
    return (addition)

print(addpoly([(5,4),(3,2)],[(-4,1),(-2,0)]))
print(addpoly([(5,3),(3,1)],[(-4,3),(-2,1)]))
print(addpoly([],[(1,1)]))
print(addpoly([(2,1)],[(-2,1)]))

def multpoly(p1,p2):
    p1=cleanup(p1)
    p2=cleanup(p2)
    multiply={}
    for i in p2:
        for j in p1:
            if i+j not in multiply.keys():
                multiply[i+j]=p2[i]*p1[j]
            else: multiply[i+j]+=(p2[i]*p1[j])
    multi=[(i,j) for i,j in zip(multiply.values(),
                                multiply.keys()) if i!=0]
    print(multi)
    return (multi)

multpoly([(3,1),(-2,0)],[(4,2),(7,1),(11,0)])
multpoly([(3,1),(-2,0)],[])
multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])






