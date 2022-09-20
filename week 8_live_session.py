# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:14:54 2022

@author: saubh
"""

'''
#for the input
line=input()
word=[]
while line:
    word.append(line)
    line=input()
word=word[1]
'''

word='abcbcabbacbzcabbacza'
def pal_finder(word='abcbcabbacba'):
    pals=[]
    '''
    for i in range(len(word)):
        wf=word[i:]
        wr=word[-len(word):-i]
    '''   
    while len(word)>1:
        count=0
        for i in range(len(word),1,-1):
            wf=word[-i:]
            wr=word[0:i]
            
            if wf==wf[::-1]:
                if len(pals)==0:
                    pals.append(wf)
                    count+=1
                elif len(wf)>=len(max(pals,key=len)):
                    pals.append(wf)
                    count+=1
            if wr==wr[::-1]:
                if len(pals)==0:
                    pals.append(wr)
                    count+=1
                elif len(wr)>=len(max(pals,key=len)):
                    pals.append(wr)
                    count+=1
            if count>0: break
            
        word=word[1:len(word)-1]
        try:
            if len(pals)!=0 and len(max(pals,key=len))>len(word):
                break
        except ValueError:
            pass
    
    res=[k for k in pals if len(k)==len(max(pals,key=len))]
    if len(pals)!=0:
        res=sorted(pals)[0]
    else: 
        res=''
    return res
res=(pal_finder('abcbcabbacbzcabbacza'))

print(len(res),res,sep='\n')
