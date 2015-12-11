from mx.DateTime.DateTime import TimeDelta
input_dict = {'a': 123, 'b': 456}
input_dict2 = {'a': (1,2,(2))}


def check_in_tuple(tup):
    for el in tup:
        print str(el) + " " + str(type(el))
        if type(el) in [list, set, dict]:
            return False
        elif type(el) is tuple:
            return check_in_tuple(el)
    return True

def test_swap_dict(input_dict):
    can_be_done =True
    for key in input_dict:
        if type(input_dict[key]) in [list, set, dict]:
            can_be_done = False
            break
        elif type(input_dict[key]) is tuple and not check_in_tuple(input_dict[key]):
            can_be_done = False
            break
    return can_be_done

print(test_swap_dict(input_dict))
