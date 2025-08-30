uprate = 0.94

for i in range(1,200):
    sol = float('inf')
    for j in range(0,i+1):
        if (j/i - uprate) < sol:
            sol = j/i - uprate

    numerator = round(abs(sol*i))
    denominator = i
    print(f'{numerator}/{denominator}')

