# Riddler-7-20-19

This is a program I used to find solutions to a recent puzzle on Nate Silver's fivethirtyeight.com. 

The problem involves being given a paper with a 4 by 4 grid and a marker. The task was to fill in the squares with the marker so that if someone took the paper and randomly cut out any 2 by 2 area without rotating it, then you could always accurately determine where the 2 by 2 area was cut out of the larger 4 by 4 paper. 

My initial solution, using 0 as a blank and 1 as a filled in section was:<br />
    0 0 0 0<br />
    0 1 1 0<br />
    0 1 1 0<br />
    0 0 0 0<br />
    
I noticed if you "fill in" the top left (or right) and bottom left (or right) squares also, then you get another solution. Additionally, you can flip all the squares to their opposite (0 to 1, 1 to 0) and this is a solution as well.

I was curious to know how many more solutions there were, so I wrote this Python script. I evaluate every possible state by treating the squares as binary digits (they have one of two possible values). Then, I iterate from 65,535 (0b1111 1111 1111 1111) to 0 (0b0000 0000 0000 0000). Rather than wrestle with converting Python's boolean values to a format I could easily use, I just used a 16 element list of 1's and counted down by programming the binary arithmetic. 

To determine if a state has only unique 2x2 cutouts, I wrote a separate module that evaluates all 9 possible cutouts and places a numerical identifier for each state in a 9 element list. I create the numerical identifier by multiplying the values of the 2x2 squares (top-left,top-right,bottom-left,bottom-right) by 1, 3, 5, and 11 respectively then adding them together. This way all possible outputs are unique. For example, if the 2x2 cutout was:<br />
0 1<br />
1 1<br />

...then the value for that cutout would be 0\*1 + 1\*3 + 1\*5 + 1\*11 = 19. 

Since each possible output is unique, I just create a list of all 9 cutout products for a given 4x4 state, and then I determine whether any repeats exist with the expression "len(mylist) <> len(set(mylist))" as sets remove repeats. 

By doing this, I found 6,188 possible solutions. I also added code to find all solutions that weren't just rotations or mirror images of the states. Doing this I found 799 'unique' states. 
