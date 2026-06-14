'''An escape-room door opens only on a rare code. A code is rare if:
• it is a four-digit number,
• it is a signal number,
• its first digit and last digit have different parity,
• it becomes happy within 100 jumps.
Write:
• different_parity(a, b)
• is_rare_code(code)
• print_rare_codes_up_to(limit) • print_first_rare_codes(count)
Escape Room Code Generator'''

# ── reused from problem 3 ──
def digit_sum(n):
    result = 0
    for i in str(n):
        result += int(i)
    return result

def is_signal(n):
    if n > 0 and (n % 3 == 0 or n % 5 == 0) and n % 7 != 0 and digit_sum(n) % 2 != 0:
        return True
    else:
        return False

# ── reused from problem 5 ──
def sum_square_digits(n):
    result = 0
    for i in str(n):
        result += int(i) ** 2
    return result

def is_happy(n):
    steps = 0
    while sum_square_digits(n) != 1 and steps < 100:
        n = sum_square_digits(n)
        steps += 1
    return n == 1

def different_parity(a, b):
    if (a % 2 == 0 and b % 2 != 0) or (b % 2 == 0 and a % 2 != 0):
        return True
    else:
        return False

def is_rare_code(n):
    if len(str(n)) == 4 and is_signal(n) and is_happy(n) and different_parity(int(str(n)[0]), int(str(n)[-1])):
        return True
    else:
        return False

def print_rare_codes_up_to(limit):
    for n in range(1000, limit + 1):
        if is_rare_code(n):
            print(n)

def print_first_rare_codes(count):
    found = 0
    current = 1000
    while found < count:
        if is_rare_code(current):
            print(current)
            found += 1
        current += 1

# Test cases
print("First 5 rare codes:")
print_first_rare_codes(5)
