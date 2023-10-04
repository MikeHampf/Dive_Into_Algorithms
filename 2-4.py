import math
import random

n=7
square = [[float('nan') for i in range(0,n)] for j in range(0,n)]

def printsquare(square):
    labels = ['['+str(x)+']' for x in range(0,len(square))]
    format_row = "{:>6}" * (len(labels)+1)
    print(format_row.format("",*labels))
    for label, row in zip(labels, square):
        print(format_row.format(label,*row))

center_i = math.floor(n/2)
center_j = math.floor(n/2)

# square[center_i][center_j] = int((n**2 + 1)/2)
# square[center_i + 1][center_j] = 1
# square[center_i - 1][center_j] = n**2
# square[center_i][center_j + 1] = n**2 + 1 - n
# square[center_i][center_j - 1] = n

def rule1(x,n,upright):
    return (x+(-1**upright) * n) % n**2

def rule2(x,n,upleft):
    return ((x+((-1)**upleft))%n**2)

def rule3(x,n,upleft):
    return ((x+((-1)**upleft * (-n+1)))%n**2)

entry_i = center_i
entry_j = center_j

where_we_can_go = ['up_left','up_right','down_left','down_right']
where_to_go = random.choice(where_we_can_go)



printsquare(square)