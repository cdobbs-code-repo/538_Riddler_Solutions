import checkdupes
import rotate
import time


start = time.time()

unique_list = []

counter = 0
counter_unique = 0
counter_90 = 0
counter_180 = 0
counter_flip_v = 0
counter_flip_h = 0
counter_flip_hv = 0

mylist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
while mylist != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
	if checkdupes.dupes_exist(mylist) == False:# and counter < 2:

		counter += 1

		if mylist not in unique_list and \
		rotate.rotate_90(mylist) not in unique_list and \
		rotate.rotate_180(mylist) not in unique_list and \
		rotate.rotate_270(mylist) not in unique_list and \
		rotate.mirror_v(mylist) not in unique_list and \
		rotate.rotate_90(rotate.mirror_v(mylist)) not in unique_list and \
		rotate.rotate_180(rotate.mirror_v(mylist)) not in unique_list and \
		rotate.rotate_270(rotate.mirror_v(mylist)) not in unique_list:
			unique_list.append(mylist[:])

			counter_unique += 1
			# now find symmetries
			if (mylist == rotate.rotate_90(mylist) or mylist == rotate.rotate_270(mylist)) and not (mylist == rotate.mirror_v(mylist) and mylist == rotate.rotate_180(rotate.mirror_v(mylist))):
				counter_90 += 1
				print(mylist)
			if mylist == rotate.rotate_180(mylist) and not (mylist == rotate.mirror_v(mylist) and mylist == rotate.rotate_180(rotate.mirror_v(mylist))):
				counter_180 += 1
			if mylist == rotate.mirror_v(mylist) and not mylist == rotate.rotate_180(rotate.mirror_v(mylist)):
				counter_flip_v += 1

			if mylist == rotate.rotate_180(rotate.mirror_v(mylist)) and not mylist == rotate.mirror_v(mylist):
				counter_flip_h += 1

			if mylist == rotate.mirror_v(mylist) and mylist == rotate.rotate_180(rotate.mirror_v(mylist)):
				counter_flip_hv += 1
	donebool = False
	end = len(mylist)-1
	last = len(mylist)-1
	while donebool == False:
		if mylist[end] == 1:
			mylist[end] = 0
			donebool = True
			if end != last:
				for i in range(end+1, last+1):
					mylist[i] = 1
		else:
			end -= 1

print("Number of solutions: ")
print(counter)
print("Number of unique solutions: ")
print(counter_unique)
print("Number of solutions that are 90 degree rotation invariant: ")
print(counter_90)
print("Number of solutions that are 180 degree rotation invariant: ")
print(counter_180)
print("Number of solutions that are mirror_h invariant: ")
print(counter_flip_h)
print("Number of solutions that are mirror_v invariant: ")
print(counter_flip_v)
print("Number of solutions that are mirror_hv invariant: ")
print(counter_flip_hv)
print("program execution time (sec):")
print(time.time() - start)
