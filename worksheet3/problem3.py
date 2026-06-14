'''Build a scanner for signal numbers. Write:
• digit_sum(n)
• is_signal(n)
• print_signals_up_to(limit) • print_first_signals(count)
Signal Number Scanner
  Signal rule: positive, divisible by 3 or 5, odd digit sum, not divisible by 7.'''

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

def print_signals_up_to(limit):
    for n in range(1, limit + 1):
        if is_signal(n) == True:
            print(n)

def print_first_signals(n):
    count = 0
    current = 1
    while count < n:
        if is_signal(current):
            print(current)
            count += 1
        current += 1

# Test
print("Signals up to 50:")
print_signals_up_to(50)

print("\nFirst 5 signals:")
print_first_signals(5)
