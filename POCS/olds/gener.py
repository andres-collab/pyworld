def fun(n):
    for i in range(n):
        yield i + 1


for un in fun(10):
    print(un)

t = [x for x in fun(20)]

print(t)
