# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:03:42 2024

@author: Dell
"""
#1a
def canbac_n(x,n):
    return x**(1/n)
#1b
def binhphuong(n):
    if n>0:
        return n**2
    else:
        return "so ko hop le, nhap lai"
#1c    
def sochan_am(n):
     return n<0 and n%2 == 0
 #1d
def ktra_so(n):
    if n<0 and n%2 !=0:
        return -1
    elif n>0 and n%2 == 0:
        return 1
        return 0
#1e
def ktra_gtri():
  n = input("nhap n:")
  if n.replace('.','',1).repalce('-','',1):
      n = float(n)
  #if n. lstrip('-').isdigit():(-)123
  #n = int(n)
 #if n.strip('-').isdigit(): (-)123(-)(-neu chuoi)
#n = int(n) 
  if -89 <= n <= 90:
    return n
    print("ko hop le, nhap lai")
    return ktra_gtri()     
if __name__=="__main__":
    print(canbac_n(8,3))
    print(binhphuong(3))
    print(sochan_am(-4))
    print(ktra_so(2))
    print(ktra_gtri())
    