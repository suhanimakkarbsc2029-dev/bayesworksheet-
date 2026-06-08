#Compute n!.
#Example: 5! = 5×4×3×2×1 = 120 Focus: accumulation through multiplication.
n=int(input(" enter the number you want to find the factorial of "))
k=1
while n>1:
     k*=n
     n-=1
print(k)