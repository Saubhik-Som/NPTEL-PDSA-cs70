#!/usr/bin/env python
# coding: utf-8

# # What is the value of f(3456) for the function below?

# In[11]:


def f(x):
    d=0
    while x >= 1:
        (x,d) = (x/7,d+1)
    return(d)


# In[12]:


f(3456)


# In[9]:


x=493/7
x


# In[10]:


d=4+1
d


# 1st x=493.714 d=1
# 2nd x= 70.5   d=2
# 3rd x=10      d=3
# 4th x=1.43    d=4
# 5th x=0.2     d=5

# # What is h(60)-h(45), given the definition of h below?

# In[16]:


def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
           s = s+i
    return(s)


# In[20]:


h(60)-h(45)


# In[17]:


h(60) #0+2+3+4+......


# In[18]:


h(45) #0+3+5+9+.....


# In[19]:


107-32


# # For what value of n would g(375,n) return 4?

# In[13]:


def g(m,n): # if n=1
    res = 0
    while m >= n: #if n<m, res=0
        (res,m) = (res+1,m/n) #375/1=375
    return(res)


# In[14]:


#this calculates the value of n where res=4
#we cannot start from 1 because 375/1 is always 375 so the program will go in a infinite loop
#running the range till 375 bcz m>=n, so if m is 375 n cannot be >375
for i in range(2,375):
    res=g(375,i)
    if res==4:
        print(i)


# correct value is 4

# # Consider the following function f:
# 

# Which of the following is correct?
#  1) The function always terminates with mys(n) = factorial of n
#  2) The function always terminates with mys(n) = 1+2+...+n
#  3) The function terminates for positive n with mys(n) = factorial of n
#  4) The function terminates for positive n with mys(n) = 1+2+...+n

# In[15]:


def mys(m):
  if m == 1:
    return(1)
  else:
    return(m+mys(m-1))


# In[17]:


mys(5)


# 1st m= 5, 5+10=15
# 2nd m=4 4+6=10
# 3rd m=3 3+3=6
# 4th m=2 2+1=3
# 5h m=1 return=1 mys(2-1)=1
# 
# 

# In[18]:


1+2+3+4+5


# In[ ]:


#if I am calling mys(m) [while m<0] it result as 1+2+3+4.....m


# In[ ]:


mys(5)


# 1st m= 5, 5+mys(5-1)
# 2nd m=2, 4+mys(4-1)
# 3rd m=3, 3+mys(3-1)
# 4th m=2, 2+mys(2-1)
# 5th m=1, return mys(2-1)=1
# .
# .
# .
# If m<0 then the function will run in an infinite loop
