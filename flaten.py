def flat(lis,depth):
    new_lis = []
    for item in lis:
	if isinstance(item, list):
           if depth>0:
                depth=depth-1
		new_lis.extend(flat(item,depth))
	   else:
		new_lis.append(item)
        else:
            new_lis.append(item)
    return new_lis


def flatten(list_a, list_b,max_depth):
	list_final=[list_a,list_b]
	xxx= flat (list_final,max_depth-1)
	return xxx



list_a=[[0, [1, 2], [3, 4, [5, [6]]], 7],32]
list_b=[43,33,[77,33,[26],4],4]


print 'list_a=',list_a
print 'list_b=',list_b
max_depth=0
while (max_depth==0) or (max_depth>5):
	max_depth = int(raw_input('max_depth (between 1 and 5) :'))


print 'flatten(list_a,list_b,max_depth)=',flatten(list_a,list_b,max_depth)

