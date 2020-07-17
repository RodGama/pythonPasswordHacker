import itertools


abc = 'abcdefghijklmnopqrstuvwxyz1234567890'
passw_2 = itertools.product(abc, abc)
for x in itertools.product(abc, abc):
    print(''.join(x))
