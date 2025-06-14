# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:58:40 2024

@author: LENOVO
"""

def f6(a,l):
    with open('a','r') as f_a:
        a = [int(line.strip()) for line in f_a]
    with open('l','r') as f_l:
        l = [int(line.strip()) for line in f_l]
    # f5 can be called here
    tot = 0
    for i in l:
        for j in a:
            if i%j == 0 :
              tot = tot + i
              break
    return tot
    #return f5(a,l)

l=list(range(12))
l.remove(10)
with open('a','w') as f:
  for n in [2,3,5]:
    f.write(str(n)+'\n')
with open('l','w') as f:
  for n in l:
    f.write(str(n)+'\n')
f6('a','l')==37


#%%

l=list(range(12))
l.remove(10)
with open('a','w') as f:
  for n in [2,3,5]:
    f.write(str(n)+'\n')
with open('l','w') as f:
  for n in l:
    f.write(str(n)+'\n')
    
    
with open('a','r') as f_a:
    a = [int(line.strip()) for line in f_a]
with open('l','r') as f_l:
    l = [int(line.strip()) for line in f_l]
tot = 0
for i in l:
    for j in a:
        if i%j == 0 :
          tot = tot + i
          break
print(tot)


