#!/usr/bin/env python3
import os.path
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gen import field, gen_random
from librip.iterators import Unique as unique


print()
path = os.path.abspath(sys.argv[1])

with open(path) as f:
    data = json.load(f)

def f1(arg):
    return(sorted([i for i in unique([j['job-name'] for j in arg], ignore_case = True)]))


def f2(arg):
	return([x for x in arg if 'программист' in x])


def f3(arg):
    return(["{} {}".format(x, "с опытом Python") for x in arg])


@print_result
def f4(arg):
    return(["{}, {} {} {}".format(x,"зарплата", y, "руб.") for x, y in zip(arg, list(gen_random(100000, 200000, len(arg))))])


with timer():
	f4(f3(f2(f1(data))))
