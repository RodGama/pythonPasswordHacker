import itertools


flower_1 = itertools.combinations(flower_names, 1)
for x in flower_1:
    print(x)
flower_2 = itertools.combinations(flower_names, 2)
for x in flower_2:
    print(x)
flower_3 = itertools.combinations(flower_names, 3)
for x in flower_3:
    print(x)
