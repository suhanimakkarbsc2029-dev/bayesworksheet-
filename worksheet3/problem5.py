'''A number is called happy if repeatedly replacing it with the sum of the squares of its digits eventually reaches 1.
Example: 19→82→68→100→1. Write:
• sum_square_digits(n) • next_happy_state(n) • is_happy(n)
• print_happy_trace(n)
Constraint: since you do not have lists or sets yet, stop after 100 jumps if you have not reached 1.
Test it on: 1, 7, 19, 20, 4, 0.'''

def sum_square_digits(n):
    result = 0
    for i in str(n):
        result += int(i) ** 2
    return result

def next_happy_state(n):
    return sum_square_digits(n)

def is_happy(n):
    steps = 0
    while next_happy_state(n) != 1 and steps < 100:
        n = next_happy_state(n)
        steps += 1
    return n == 1

def print_happy_trace(n):
    steps = 0
    while n != 1 and steps < 100:
        print(n, end=" → ")
        n = next_happy_state(n)
        steps += 1
    print(n)

# Test cases
for n in [1, 7, 19, 20, 4, 0]:
    print(f"n={n} | happy={is_happy(n)}")
    print_happy_trace(n)
    print()
