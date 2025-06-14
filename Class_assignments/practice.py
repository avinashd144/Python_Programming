# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 23:03:31 2024

@author: LENOVO
"""

l = list(range(10))
print(l)
for i in l:
    print(i)
    if i%3 == 0:
        #print('ok') 
        pass
    else:
        #l.remove(i)
        #print(i)
        pass
        
        
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

        