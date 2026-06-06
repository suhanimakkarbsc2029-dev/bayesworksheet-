#Given a number N, print every prime number ≤ N.
#Example: if N = 20, the output should be 2, 3, 5, 7, 11, 13, 17, 19.
n=int(input("enter any number"))
root=int(n**0.5+1)
num=2
while num<=n:
    root=int(num**0.5)+1
    is_prime=True
    i=2
    for i in range(2, root):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
    num+=1
     


   