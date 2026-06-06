num = int(input("enter any number: "))

if num < 2:
    print("it is not prime")
elif num == 2:
    print("it is prime")
else:
    root = int(num**0.5) + 1
    is_prime = True
    for i in range(2, root):
        if num % i == 0:
            is_prime = False
            break
    print("it is prime" if is_prime else "it is not prime")
