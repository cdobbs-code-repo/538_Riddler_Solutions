#fivethirtyeight
import math
from itertools import combinations 
from numpy import array
# v = array([1, 2, 3])
# print(v)

#model = [i,j]
twelve = [0,1]
one    = [0.5,math.sqrt(3)/2]
two    = [math.sqrt(3)/2,0.5]
three  = [1,0]
four   = [math.sqrt(3)/2,-0.5]
five   = [0.5,-math.sqrt(3)/2]
six    = [0,-1]
seven  = [-0.5,-math.sqrt(3)/2]
eight  = [-math.sqrt(3)/2,-0.5]
nine   = [-1,0]
ten    = [-math.sqrt(3)/2,0.5]
eleven = [-0.5,math.sqrt(3)/2]

options = [one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve]


# now get all combinations
comb = combinations(options, 7) 

for each in comb:
    temp = array([0,0])
    for elem in each:
        temp = array(elem) + temp
    if temp[0] < 0.001 and temp[0] > -0.001 and temp[1] < 0.001 and temp[1] > -0.001:
        print("success with:")
        print(each)
