def field(items, *args):
    assert len(args) > 0, 'No args'
    if len(args) == 1:
        for elem in items:
            yield elem[args[0]]
    else:
        dict = {}
        for elem in items:
            for arg in args:
                dict[arg] = elem[arg]
            yield dict

def gen_random(begin, end, num_count):
    pass
    for i in range(num_count):
    	yield randint(begin, end)
