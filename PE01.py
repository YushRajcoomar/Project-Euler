import math

workingrange = list(range(1000))[1:]

def is5or3(lis):
    alis = []
    for x in lis:
        if x % 5 == 0:
            alis.append(x)
        elif x % 3 == 0:
            alis.append(x)
    print sum(alis)

is5or3(workingrange)

