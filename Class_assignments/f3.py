# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:08:29 2024

@author: LENOVO
"""
#%% Problem statement and hints
#Create a function to find the sum of all the multiples of a or b in l.
##(a,b,l) are function parameters, l is a list.
def f3(a,b,l):
  pass
l=list(range(1000))
l.remove(168)
f3(3,5,l)==233000


#%%
l=list(range(10))
print(l)
for i in l:
  #print(i)
  if i%5 == 0 or i%3 == 0:
      print(i)
      l.remove(i)
print(l)
      

#%%
l=list(range(10))
print(l)
l1 = list()
for i in l:
  #print(i)
  if i%5 == 0 or i%3 == 0:
      print(i)
      l1.append(i)
l = l1
print(l)
a = sum(l)
type(a)
sum(l)
      
#%%
def f3(a,b,l):
    l1 = list()
    for i in l:
      if i%a == 0 or i%b == 0:
          #print(i)
          l1.append(i)
    #print(l1)
    l = l1
    a = sum(l)
    print(a)
    return a

l=list(range(1000))
l.remove(168)
f3(3,5,l)==233000

#%% 
def tot(a,b):
    y = a+b
    y
    print(y)
    return y
    
tot(2,5)==7
    
    
    
    
    
    
    
    
    
    