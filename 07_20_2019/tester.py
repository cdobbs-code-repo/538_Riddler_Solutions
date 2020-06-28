import checkdupes
import rotate

unique_list = []
mylist = [0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0]

print(checkdupes.dupes_exist(mylist))

if mylist not in unique_list and \
                rotate.rotate_90(mylist) not in unique_list and \
                rotate.rotate_180(mylist) not in unique_list and \
                rotate.rotate_270(mylist) not in unique_list and \
                rotate.mirror_v(mylist) not in unique_list and \
                rotate.rotate_90(rotate.mirror_v(mylist)) not in unique_list and \
                rotate.rotate_180(rotate.mirror_v(mylist)) not in unique_list and \
                rotate.rotate_270(rotate.mirror_v(mylist)) not in unique_list:
	unique_list.append(mylist)
	print(unique_list)
