
def mirror_v(myl):
	newlist = [myl[3],myl[2],myl[1],myl[0],\
                myl[7],myl[6],myl[5],myl[4],\
                myl[11],myl[10],myl[9],myl[8],\
                myl[15],myl[14],myl[13],myl[12]]
        return newlist

#Note: mirror_h = rotate_180(mirror_v(myl))

def rotate_90(myl):
	newlist = [myl[12],myl[8],myl[4],myl[0],\
		myl[13],myl[9],myl[5],myl[1],\
		myl[14],myl[10],myl[6],myl[2],\
		myl[15],myl[11],myl[7],myl[3]]
	return newlist

def rotate_180(myl):
	newlist = [myl[15],myl[14],myl[13],myl[12],\
                myl[11],myl[10],myl[9],myl[8],\
                myl[7],myl[6],myl[5],myl[4],\
                myl[3],myl[2],myl[1],myl[0]]
        return newlist

def rotate_270(myl):
	newlist = [myl[3],myl[7],myl[11],myl[15],\
                myl[2],myl[6],myl[10],myl[14],\
                myl[1],myl[5],myl[9],myl[13],\
                myl[0],myl[4],myl[8],myl[12]]
        return newlist

#print(mirror_v([1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0]))
