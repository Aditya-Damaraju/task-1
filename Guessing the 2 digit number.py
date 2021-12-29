import random
import math
user_name = str(input("Enter your name:"))
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the higher limit: "))
jarvis_choice = random.randint(lower, upper)
print("\n\tYou have only ",
	round(math.log(upper - lower + 1, 2)),
	"chances to guess the integer", str(user_name))
count = 0
while count < math.log(upper - lower + 1, 2):
	count += 1
	guess = int(input("Guess the number: "))
	if jarvis_choice == guess:
		print("Congratulations", str(user_name), "you guessed the number in ",
         count, "attempts")
	
		break
	elif jarvis_choice > guess:
		print("Your guessed number is too low!")
	elif jarvis_choice < guess:
		print("Your guessed number is too high!")
if count >= math.log(upper - lower + 1, 2):
	print("\n The number is %d" % jarvis_choice)
	print("\t Better Luck Next time!")
exit (0)