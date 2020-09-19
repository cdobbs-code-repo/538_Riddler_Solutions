#9_19_20_classic


import random
import numpy
from scipy import stats


iter_list = []

for x in range(0,1000000):

    foo = random.randint(1,267751)

    bar = 267751
    found = False
    iterations = 0
    mini = 1
    maxi = 267751

    while not found:
        iterations += 1
        bar = (mini + maxi) / 2
        if bar % 1 != 0:
            updown = random.randint(1,2)
            if updown == 1:
                bar = int(bar)
            else:
                bar = int(bar) + 1
        else:
            bar = int(bar)
        if foo == bar:
            found = True
            #print("iterations: " + str(iterations))
            iter_list.append(iterations)
        elif bar < foo:
            mini = bar + 1
        else:
            maxi = bar - 1

print(numpy.mean(iter_list))
print(numpy.median(iter_list))
print(stats.mode(iter_list))

final = {}
for x in range(1,21):
    temp = 0
    for myiter in iter_list:
        if x == myiter:
            temp += 1
    final.update({x:temp})

print(final)