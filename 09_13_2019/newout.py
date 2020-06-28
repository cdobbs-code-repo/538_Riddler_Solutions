

file = open("output.txt", "r")
newfile = open("newout.txt","w")
for line in file:
	for x in range(0, len(line)):
		if x % 30 == 0:
			newfile.write("\n")
		else:
			newfile.write(line[x])

file.close()
newfile.close()
