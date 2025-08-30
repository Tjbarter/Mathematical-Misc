
def twin_primes(s, n):
    list = []
    for i in range(s, n):
        for j in range(1, i):
            if i % j == 0 and j != 1:
                break
            elif j == i-1:
                list.append(i)
    for i in range(0, len(list)-1):
        if list[i+1] - list[i] == 2:
            print(list[i], list[i+1])
twin_primes(2, 100)



def triplets(s, n):
    for i in range(s, n):
        for j in range(s, n):
            if (i**2 + j**2) % ((i**2 + j**2)**0.5) == 0 and j > i:
                print(f'{i}^2 + {j}^2 = {(round((i**2 + j**2)**0.5))}^2')
# triplets(1, 150)
