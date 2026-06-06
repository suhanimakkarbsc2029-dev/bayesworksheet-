#Start with two numbers: 0 and 1. Keep making the next number by adding the previous two. Print the first 10 values. What pattern emerges?
x=0
y=1
for i in range(10):
    print(x+y)
    x+=1
    y+=1
    
"the pattern is that they are first 10 odd numbers"

#same thing using while loop
x,y=0,1
iterations=0
while iterations<=10:
    print(x+y)
    x+=1
    y+=1
    iterations+=1
    