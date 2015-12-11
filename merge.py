def combineDicts(stringuunu, stringudoi):
    output = {}
    for item, value in stringuunu.iteritems():
        if stringudoi.has_key(item):
            if isinstance(stringudoi[item], dict):
                output[item] = combineDicts(value, stringudoi.pop(item))
            else:
 	    	if type(value)==type(stringudoi[item]):
			if ((isinstance(stringudoi[item], str)) or (isinstance(stringudoi[item], int))):
				output[item] = value + (stringudoi.pop(item))
			else:
				if (isinstance(stringudoi[item], set)):
					output[item] = set(value).union(set(stringudoi.pop(item)))
				else:
			               	output[item] = value
					output[item].extend(stringudoi.pop(item))

		else:
			temp = (value,stringudoi.pop(item))
			output[item] = tuple(temp)
	else:
	    output[item]=stringuunu[item]
    for item, value in stringudoi.iteritems():
         output[item] = stringudoi.pop(item)
    return output


a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

print combineDicts(a,b)
