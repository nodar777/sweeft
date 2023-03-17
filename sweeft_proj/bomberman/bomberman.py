import math
import os
import re
import random
import sys
r = 4
c = 5
def bomber_man(n, grid):
    if n == 1:
        return grid

    if n%2 == 0:
        return ['O'*c for i in range(r)]
    
    n //= 2
    for q in range((n+1) % 2 + 1):
        newgrid = [['O']*c for i in range(r)]
        
        def set(x, y):
            if 0 <= x <= r and 0 <= y <= c:
                newgrid[x][y] = '.'
                
        xi = [0,0,0,1,-1]
        yi = [0,-1,1,0,0]
        
        for x in range(r):
            for y in range(c):
                if grid[x][y] =='O':
                    for i,j in zip(xi, yi):
                        set(x+i, y+j)
                        
        grid = newgrid
    return ["".join(x) for x in grid] 


n1 =[".....", "..O..", ".....","....."]
a = bomber_man(3, n1)
print(a)

#mas shemdeg rac tqveni aqseleraciis programis shesaxeb gavige bevrad ufro met dros vutmob piTons da 
#djangos, gpirdebiT ufro metsac gavakeTeb.

