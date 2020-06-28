#newlist = [myl[0]*1 + myl[1]*3 + myl[4]*5 + myl[5]*11,\
#        myl[1]*1 + myl[2]*3 + myl[5]*5 + myl[6]*11,\
#        myl[2]*1 + myl[3]*3 + myl[6]*5 + myl[7]*11,\
#        myl[4]*1 + myl[5]*3 + myl[8]*5 + myl[9]*11,\
 #       myl[5]*1 + myl[6]*3 + myl[9]*5 + myl[10]*11,\
  #      myl[6]*1 + myl[7]*3 + myl[10]*5 + myl[11]*11,\
   #     myl[8]*1 + myl[9]*3 + myl[12]*5 + myl[13]*11,\
    #    myl[9]*1 + myl[10]*3 + myl[13]*5 + myl[14]*11,\
     #   myl[10]*1 + myl[11]*3 + myl[14]*5 + myl[15]*11]


#mylist = [1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0]
#mylist = [0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0]

def dupes_exist(myl):
	newlist = [myl[0]*1 + myl[1]*3 + myl[4]*5 + myl[5]*11,\
        myl[1]*1 + myl[2]*3 + myl[5]*5 + myl[6]*11,\
        myl[2]*1 + myl[3]*3 + myl[6]*5 + myl[7]*11,\
        myl[4]*1 + myl[5]*3 + myl[8]*5 + myl[9]*11,\
        myl[5]*1 + myl[6]*3 + myl[9]*5 + myl[10]*11,\
        myl[6]*1 + myl[7]*3 + myl[10]*5 + myl[11]*11,\
        myl[8]*1 + myl[9]*3 + myl[12]*5 + myl[13]*11,\
        myl[9]*1 + myl[10]*3 + myl[13]*5 + myl[14]*11,\
        myl[10]*1 + myl[11]*3 + myl[14]*5 + myl[15]*11]
	#print(newlist) #debug
	return len(newlist) <> len(set(newlist))
#print(dupes_exist(mylist))
