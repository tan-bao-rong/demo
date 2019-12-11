#! /usr/bin/env python3
i = 1
j = 1
print ('---'*20)
for i in range(1,10):
    for j in range(1,10):
        print ('{:1d}*{:1d}={:2d}'.format(i,j,i*j),end='  ')
    print(' ')
print ('---'*20)
