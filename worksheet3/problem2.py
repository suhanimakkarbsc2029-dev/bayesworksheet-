'''Build a launch checker for drone missions. Write:
• battery_needed(distance, windy)
• can_launch(distance, battery, windy)
• safety_margin(distance, battery, windy)
• print_mission_report(distance, battery, windy)
Drone Return-to-Base Checker
  Rule: each kilometre must be flown twice: out and back. Calm costs 4 per km, windy costs 6 per km, reserve is 15.
 Computational Thinking 7 When the Machine Has to Delegate
Bayes Institute | Module 1: The Three Code Flows WS-03
  Test it on: (8, 90, False), (8, 90, True), (3, 40, True), (0, 15, False).'''

def battery_needed(distance, windy):
    if windy == True:
        return distance * 6 * 2
    else:
        return distance * 4 * 2

def can_launch(distance, battery, windy):
    if (battery - battery_needed(distance, windy)) >= 15:
        return "Launch"
    else:
        return "Do not launch"

def safety_margin(distance, battery, windy):
    margin = (battery - battery_needed(distance, windy)) - 15
    return margin

def print_mission_report(distance, battery, windy):
    print(f"Distance: {distance} km | Battery: {battery} | Windy: {windy} | Status: {can_launch(distance, battery, windy)} | Margin: {safety_margin(distance, battery, windy)}")

# Test cases
missions = [(8, 90, False), (8, 90, True), (3, 40, True), (0, 15, False)]
for distance, battery, windy in missions:
    print_mission_report(distance, battery, windy)
