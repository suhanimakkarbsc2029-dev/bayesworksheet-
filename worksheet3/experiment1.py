'''A museum lock accepts a code if all of these are true: • it is a four-digit number,
• the sum of its digits is divisible by 7,
• the first digit is smaller than the last digit,
Museum Lock Codes
  • it is not divisible by 5.
Check the codes 1729, 2468, 7007, 8351, and 9999. Write the logic separately each time. Then
change the digit-sum rule from "divisible by 7" to "divisible by 9"'''

# --- Rule: divisible by 7 ---

# Code: 1729
d1,d2,d3,d4 = 1,7,2,9
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%7==0 and number%5!=0:
    print("1729: accepted")
else:
    print("1729: not accepted")

# Code: 2468
d1,d2,d3,d4 = 2,4,6,8
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%7==0 and number%5!=0:
    print("2468: accepted")
else:
    print("2468: not accepted")

# Code: 7007
d1,d2,d3,d4 = 7,0,0,7
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%7==0 and number%5!=0:
    print("7007: accepted")
else:
    print("7007: not accepted")

# Code: 8351
d1,d2,d3,d4 = 8,3,5,1
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%7==0 and number%5!=0:
    print("8351: accepted")
else:
    print("8351: not accepted")

# Code: 9999
d1,d2,d3,d4 = 9,9,9,9
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%7==0 and number%5!=0:
    print("9999: accepted")
else:
    print("9999: not accepted")

print()
print("--- Now with divisible by 9 rule ---")
print()

# --- Rule changed: divisible by 9 ---

# Code: 1729
d1,d2,d3,d4 = 1,7,2,9
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%9==0 and number%5!=0:
    print("1729: accepted")
else:
    print("1729: not accepted")

# Code: 2468
d1,d2,d3,d4 = 2,4,6,8
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%9==0 and number%5!=0:
    print("2468: accepted")
else:
    print("2468: not accepted")

# Code: 7007
d1,d2,d3,d4 = 7,0,0,7
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%9==0 and number%5!=0:
    print("7007: accepted")
else:
    print("7007: not accepted")

# Code: 8351
d1,d2,d3,d4 = 8,3,5,1
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%9==0 and number%5!=0:
    print("8351: accepted")
else:
    print("8351: not accepted")

# Code: 9999
d1,d2,d3,d4 = 9,9,9,9
number = d1*1000 + d2*100 + d3*10 + d4
if d1<d4 and (d1+d2+d3+d4)%9==0 and number%5!=0:
    print("9999: accepted")
else:
    print("9999: not accepted")
