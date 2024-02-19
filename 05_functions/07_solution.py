def sum_all(*args):
    print(args)
    print(*args)
    return sum(args)

print(sum_all(1,4,4,5))