N = int(input("Enter the number you want triplets from: "))

found = False
for a in range(1, N+1):
    for b in range(a, N+1):
        for c in range(b, N+1):
            if a**2 + b**2 == c**2:
                print(a, b, c)
                found = True

if not found:
    print(N, "doesn't have a triplet")
