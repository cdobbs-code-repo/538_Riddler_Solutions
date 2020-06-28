import time

file = open("output.txt","w")

start = time.time()

states = ['AL','AK','AS','AZ','AR','CA','CO','CT','DE','DC','FM','FL','GA','GU','HI','ID','IL','IN','IA','KS','KY','LA','ME','MH','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','MP','OH','OK','OR','PW','PA','PR','RI','SC','SD','TN','TX','UT','VT','VI','VA','WA','WV','WI','WY']

start_iter = 1
start_string = ""
max = 0

def find_longest(iter,mystring):
	if iter >= 31:
		file.write(mystring[:-1])
	get_max_iter(iter)
	if iter == 1:
		for abr in states:
			print(abr)
			find_longest(iter+1,abr)
	else:
		if repeat_exists(mystring):
			return
		else:
			for abr in states:
				if abr[0] == mystring[-1]:
					find_longest(iter+1,mystring+abr[1])

def repeat_exists(foo):
	bar = []
	for i in range(0,len(foo)-1):
		temp = foo[i] + foo[i+1]
		#print(temp)
		bar.append(temp)
	#print(bar)
	return not( len(bar) == len(list(dict.fromkeys(bar))) )

def get_max_iter(foo):
	global max
	if foo > max:
		max = foo

find_longest(1,"")

print(max)

print(time.time() - start)





