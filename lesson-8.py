def func(*args):
    if len(args) == str:
         print("NOOO!")
    else:
        res = [
            {

            arg:arg+1

        }
        for arg in args
        ]
        yield res
print(next(func(2, 3, 4, 5)))

#2
def func2(limit):
    caunt = 0
    for lim in range(limit):
        if lim % 2 != 0:
            yield lim
            caunt+=1
            if caunt >= 3:
                break
new = func2(10)
for new2 in new:
    print(new2)
