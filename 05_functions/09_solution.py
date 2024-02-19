def even_generateor(limit):
    for i in range(2,limit + 1, 2):
        yield i

for num in even_generateor(10):
    print(num)