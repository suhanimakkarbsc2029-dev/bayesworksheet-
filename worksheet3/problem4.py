'''For a positive integer n, repeatedly apply:
n/2      if n is even
3n+1     if n is odd
Collatz Flight Recorder
  Stop when the value reaches 1. Write:
• next_collatz(n) • steps_to_one(n) • peak_value(n)'''

def next_collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def steps_to_one(n):
    count = 0
    while next_collatz(n) > 1:
        n = next_collatz(n)
        count = count + 1
    return count

def peak_value(n):
    peak = n
    while next_collatz(n) > 1:
        n = next_collatz(n)
        if n > peak:
            peak = n
    return peak

def print_flight_report(n):
    print(f"n={n} | steps={steps_to_one(n)} | peak={peak_value(n)}")

# Test cases
for n in [1, 2, 3, 6, 7, 27]:
    print_flight_report(n)