# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

first_goal = "Ruud Gullit"
second_goal = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = f"{first_goal} {goal_0}, {second_goal} {goal_1}"
report = f"{first_goal} scored in the {goal_0}nd minute\n{second_goal} scored in the {goal_1}th minute"

print(scorers)
print(report)

player = "Hans van Breukelen"
first_name = player[0:4]
last_name_len = len(player[5:])
name_short = f"{player[0]}." + player[4:]
chant = f"{first_name}!" f" {first_name}!" f" {first_name}!" f" {first_name}!" 
good_chant = chant[4] != ' '

print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)