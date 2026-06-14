'''Call a number a signal number if:
• it is positive,
• it is divisible by 3 or 5,
• its digit sum is odd,
• it is not divisible by 7.
Signal Numbers
  First print all signal numbers up to 80.
  Then print the first 20 signal numbers.
  Use only loops and branches for now.'''

# All signal numbers up to 80
print("Signal numbers up to 80:")
for n in range(1, 81):
    digit_sum = 0
    for i in str(n):
        digit_sum += int(i)
    if n > 0 and (n % 3 == 0 or n % 5 == 0) and digit_sum % 2 != 0 and n % 7 != 0:
        print(n)

# First 20 signal numbers
print("\nFirst 20 signal numbers:")
count = 0
current = 1
while count < 20:
    digit_sum = 0
    for i in str(current):
        digit_sum += int(i)
    if current > 0 and (current % 3 == 0 or current % 5 == 0) and digit_sum % 2 != 0 and current % 7 != 0:
        print(current)
        count += 1
    current += 1
