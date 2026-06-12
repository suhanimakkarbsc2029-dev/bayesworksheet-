#Convert a binary number into decimal.
#Example: 10112 =1×8+0×4+1×2+1×1=11 Focus: positional reasoning. Each digit has a place value.#


num = str(input("enter the number "))
result= 0
for i,char in enumerate(num):
  result += int(char) * 2 **(len(num) - i - 1)
print(result)