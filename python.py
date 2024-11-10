# Python code to play the 21 Number Game.
# In this game, players take turns to count up to 21 by adding a number from 1 to 3.
# The player who reaches 21 loses the game.

# Returns the nearest multiple of 4 that is greater than or equal to the given number.
def nearestMultiple(num):
	if num >= 4:
		near = num + (4 - (num % 4))
	else:
		near = 4
	return near

# Prints a loss message and ends the game.
def lose1():
	print("\n\nYOU LOSE!")
	print("Better luck next time!")
	exit(0)

# Checks if the elements in the list are consecutive numbers.
def check(xyz):
	i = 1
	while i < len(xyz):
		if (xyz[i] - xyz[i - 1]) != 1:
			return False
		i += 1
	return True

# Starts the 21 Number Game and manages the gameplay.
def start1():
	xyz = []  # Holds the sequence of numbers entered by both player and computer.
	last = 0  # Tracks the last number in the sequence.
	while True:
		print("Enter 'F' to take the first turn.")
		print("Enter 'S' to take the second turn.")
		chance = input('> ')

		# Player chooses to take the first turn.
		if chance == "F":
			while True:
				if last == 20:
					lose1()
				else:
					print("\nYour turn.")
					print("How many numbers do you want to enter (1-3)?")
					inp = int(input('> '))

					# Validates player input.
					if 0 < inp <= 3:
						comp = 4 - inp
					else:
						print("Invalid input. You are disqualified from the game.")
						lose1()

					i = 1
					print("Enter your numbers:")

					# Player enters chosen numbers.
					while i <= inp:
						a = int(input('> '))
						xyz.append(a)
						i += 1

					# Updates last with the final number from player's input.
					last = xyz[-1]

					# Checks if the player's numbers are consecutive.
					if check(xyz):
						if last == 21:
							lose1()
						else:
							# Computer's turn to add numbers to the sequence.
							j = 1
							while j <= comp:
								xyz.append(last + j)
								j += 1
							print("Order of inputs after computer's turn:")
							print(xyz)
							last = xyz[-1]
					else:
						print("You did not enter consecutive integers.")
						lose1()

		# Player chooses to take the second turn.
		elif chance == "S":
			comp = 1
			last = 0
			while last < 20:
				# Computer's turn to add numbers.
				j = 1
				while j <= comp:
					xyz.append(last + j)
					j += 1
				print("Order of inputs after computer's turn:")
				print(xyz)

				if xyz[-1] == 20:
					lose1()
				else:
					print("\nYour turn.")
					print("How many numbers do you want to enter (1-3)?")
					inp = int(input('> '))
					i = 1
					print("Enter your numbers:")

					# Player enters their numbers.
					while i <= inp:
						xyz.append(int(input('> ')))
						i += 1
					last = xyz[-1]

					# Checks if the player's numbers are consecutive.
					if check(xyz):
						near = nearestMultiple(last)
						comp = near - last
						if comp == 4:
							comp = 3
					else:
						print("You did not enter consecutive integers.")
						lose1()
			print("\n\nCONGRATULATIONS!!!")
			print("YOU WON!")
			exit(0)
		else:
			print("Invalid choice.")

# Main game loop to start the game or allow the player to quit.
game = True
while game:
	print("Player 2 is the computer.")
	print("Do you want to play the 21 Number Game? (Yes / No)")
	ans = input('> ')
	if ans == 'Yes':
		start1()
	else:
		print("Do you want to quit the game? (yes / no)")
		nex = input('> ')
		if nex == "yes":
			print("Quitting the game...")
			exit(0)
		elif nex == "no":
			print("Continuing...")
		else:
			print("Invalid choice.")
