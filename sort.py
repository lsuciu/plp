to_sort=[]
dictionar={}
id=0
dictx={}
f = open('file', 'r')
list=(f.readlines())
for line in list:
	words=(line.strip().split('\n'))[0].split(' ')
	if words[0]!='':
		dictionar.update(dict({words[0]:words[1]}))
	else:
		keys = sorted(dictionar.keys())
		print keys
		id=id+1
		to_sort.append(dict({id:dictionar}))
		dictionar={}
		
keys = sorted(dictionar.keys())
print keys
id=id+1
to_sort.append(dict({id:dictionar}))
f.close()




print to_sort


