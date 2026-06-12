#Take an integer and compute the sum of its digits. Example: 4832→4+8+3+2=17
#Constraint: Do it once using arithmetic: repeated % 10 and // 10. Then compare with a string-based version.


num=int(input("enter the integer you want to check"))  
result=0
while num!=0:
 digit=num%10
 num=num//10
 result+=digit
print(result)

#using strings
num=str(input("enter the integer you want to check")) 
result=0
for char in num:
  result+=int(char)
print(result)