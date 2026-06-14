'''Build a tiny fraud warning rule. A transaction gains:
• 2 points if amount > 10000,
• 1 point if hour < 6 or hour > 22,
• 1 point if balance after payment would be below 500,
• 2 points if amount is more than half the current balance.
Transaction Suspicion Score
  Print "Block" if the score is at least 3, otherwise print "Allow".
  Try three transactions. Then change the block threshold from 3 to 4.'''

BLOCK_THRESHOLD = 4

# Transaction 1
amount = 12000
hour = 23
balance = 15000

score = 0
if amount > 10000:
    score += 2
if hour < 6 or hour > 22:
    score += 1
if balance - amount < 500:
    score += 1
if amount > balance / 2:
    score += 2

if score >= BLOCK_THRESHOLD:
    print(f"Transaction 1: Block (score={score})")
else:
    print(f"Transaction 1: Allow (score={score})")

# Transaction 2
amount = 200
hour = 10
balance = 1000

score = 0
if amount > 10000:
    score += 2
if hour < 6 or hour > 22:
    score += 1
if balance - amount < 500:
    score += 1
if amount > balance / 2:
    score += 2

if score >= BLOCK_THRESHOLD:
    print(f"Transaction 2: Block (score={score})")
else:
    print(f"Transaction 2: Allow (score={score})")

# Transaction 3
amount = 8000
hour = 2
balance = 9000

score = 0
if amount > 10000:
    score += 2
if hour < 6 or hour > 22:
    score += 1
if balance - amount < 500:
    score += 1
if amount > balance / 2:
    score += 2

if score >= BLOCK_THRESHOLD:
    print(f"Transaction 3: Block (score={score})")
else:
    print(f"Transaction 3: Allow (score={score})")
