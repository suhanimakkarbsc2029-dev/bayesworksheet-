# Hint: Repeatedly divide by 2. The remainders tell the story, but not in the order you first see them.
#Test it on: 0, 1, 2, 5, 13, 32

num=int(input("enter any integer"))

result=""

if num ==0:
    result = "0"
while num > 0:
    result = str(num%2)+result
    num = num//2

print(result)