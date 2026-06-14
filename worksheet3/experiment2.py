'''A drone needs battery to fly out and return. Assume each kilometre costs 4 battery units in calm weather and 6 in windy weather. The drone must also keep 15 units as reserve.
Check these missions:
• distance = 8 km, battery = 90, windy = False • distance = 8 km, battery = 90, windy = True • distance = 3 km, battery = 40, windy = True
Print "Launch" or "Do not launch". Then change the reserve from 15 to 25.


battery=int(input("enter the no. of battery units "))
distance=int(input("enter distance "))
windy=str(input(" state whether it was windy or not yes or no"))

if windy==str("yes"):
    windy=True
elif windy==str("no"):
    windy=False


if windy == False:
    if battery - (distance * 4 * 2) >= 25:
        print("Launch")
    else:
        print("Do not launch")
elif windy == True:
    if battery - (distance * 6 * 2) >= 25:
        print("Launch")
    else:
        print("Do not launch")'''
        

digits=str(input("num"))
d1,d2,d3,d4=int(digits.split())