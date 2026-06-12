#Given two integers, compute their GCD and LCM. Version 1: Try iterative divisor checking.
#Version 2: Try the Euclidean algorithm. Then: derive LCM from GCD.

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

# Version 1: Iterative
gcd1 = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd1 = i
print("Version 1 - GCD:", gcd1, " LCM:", (a * b) // gcd1)

# Version 2: Euclidean
x, y = a, b
while y != 0:
    x, y = y, x % y
print("Version 2 - GCD:", x, " LCM:", (a * b) // x)
