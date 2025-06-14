# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:23:31 2024

@author: LENOVO
"""
#%% Problem statement and hints
#2
#Create a function to find the sum of all the multiples of elements of a in l.
##(a,l) are function parameters - lists. len (a) == 2

def f4(a,l):
  pass
l=list(range(1000))
l.remove(168)
f4([3,5],l)==233000

#%% Problem statement and hints
#3
#Create a function to find the sum of all the multiples of elements of a in l.
##(a,l) are function parameters - lists.
def f5(a,l):
  pass
l=list(range(12))
l.remove(10)
f5([2,3,5],l)==37

#note this must also work for more than 3 factors - do not hardcode as 3

#%%
l=list(range(1000))
#print(l)
l1 = list()
a = [3,5]
print(a)
print("a:",sum(a))
for i in l:
  for j in a:
      if i%j == 0 :
          if i in l1:
              continue
          else:
              l1.append(i)
l = l1
#print(l)
a = sum(l)
print(a)



#%%
def f4(a,l):
    l1 = list()
    for i in l:
      for j in a:
          if i%j == 0 :
              if i in l1:
                  continue
              else:
                  l1.append(i)
    l = l1
    a = sum(l)
    print(a)
    return a
      
l=list(range(1000))
l.remove(168)
f4([3,5],l)==233000

#%%
def f5(a,l):
    l1 = list()
    for i in l:
      for j in a:
          if i%j == 0 :
              if i in l1:
                  continue
              else:
                  l1.append(i)
    l = l1
    a = sum(l)
    print(a)
    return a
      

l=list(range(12))
l.remove(10)
f5([2,3,5],l)==37


#%%
l=list(range(10))
print(l)
a=[3,5]
tot = 0
for i in l:
    for j in a:
        if i%j == 0 :
            tot = tot + i
            break
print(tot)


#%%
def f5(a,l):
  tot = 0
  for i in l:
    for j in a:
      if i%j == 0 :
        tot = tot + i
        break
  return tot
  print(tot)
#%%
l=list(range(12))
l.remove(10)
f5([2,3,5],l)==37






