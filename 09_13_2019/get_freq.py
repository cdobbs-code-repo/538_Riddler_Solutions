

file = open("newout.txt","r")

mylist = []
freq_list = []

for line in file:
	if line[-3:] in mylist:
		freq_list[mylist.index(line[-3:])] += 1
	else:
		mylist.append(line[-3:])
		freq_list.append(0)
		freq_list[mylist.index(line[-3:])] = 1

print(mylist)
print(freq_list)
