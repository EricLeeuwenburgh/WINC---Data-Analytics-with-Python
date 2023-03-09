# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

first_goal = "Ruud Gullit"
second_goal = "Marco van Basten"

goal_0 = 32    #minute the goal was mades
goal_1 = 54    #minute the goal was made

scorers = first_goal + " " + str(goal_0) + ", " + second_goal + " " + str(goal_1)
report = f"{first_goal} scored in the {goal_0}nd minute\n{second_goal} scored in the {goal_1}th minute"

print(scorers)
print(report)

player = "Hans van Breukelen"
first_name_index = player.find(" ")       # .find() = search and give back the index up to the found variable
first_name = player[0:first_name_index]
last_name = player[first_name_index+1:]
last_name_len = len(last_name)
name_short = first_name[0] + ". " + last_name
chant = (len(first_name)-1) * (first_name + "! ") + (first_name + "!")
good_chant = chant[-1] != ' '

print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)