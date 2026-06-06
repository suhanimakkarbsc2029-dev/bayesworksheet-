#Check every number from 1 to 30. Print the number if it is divisible by 3 but not by 2. Do not optimise. First make the loop honest.

        
for i in range(1, 31):
    if i % 3 == 0 and i % 2 != 0:
        print(i)
