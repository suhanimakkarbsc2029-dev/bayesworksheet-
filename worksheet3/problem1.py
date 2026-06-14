'''Build a lock-code judge for the museum rule from Experiment A. Write:
• digit_sum(n)
• first_digit(n)
• last_digit(n)
• is_valid_lock_code(code) • next_valid_code(start)
Museum Lock Code Judge
  Test it on: 999, 1000, 1729, 2468, 7007, 8351, 9999.'''

def digit_sum(digits):
    result = 0
    for i in digits:
        result += int(i)
    return result

def first_digit(digits):
    return str(digits)[0]

def last_digit(digits):
    return str(digits)[-1]

def is_valid_lock_code(digits):
    digits = str(digits)
    if digit_sum(digits) % 7 == 0 and len(digits) == 4 and first_digit(digits) < last_digit(digits):
        return "its valid"
    else:
        return "its invalid"

def next_valid_code(digits):
    digits = str(digits)
    while is_valid_lock_code(digits) == "its invalid":
        digits = str(int(digits) + 1)
    return digits

# Test cases
test_codes = [999, 1000, 1729, 2468, 7007, 8351, 9999]
for code in test_codes:
    print(code, "->", is_valid_lock_code(code))

print("Next valid after 1729:", next_valid_code(1729))
