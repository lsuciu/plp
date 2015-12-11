tree = ("b", ("a", None, None), ("z", ("c", None, None), ("zz", None, None)))


def do(tree):
    yield tree[0]
    if tree[1] is not None:
        for el in do(tree[1]):
            yield el
    if tree[2] is not None:
        for el in do(tree[2]):
            yield el

print [el for el in do(tree)]
