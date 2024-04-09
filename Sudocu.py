import sys
import re
from tabulate import tabulate

row = 9
cols = 9

def main():
	print("ENTER THE SUDOCU")
	form = []
	#DONE TODO 1: reask the user if the input is not correct
	#! TODO 2: except keybord interuption, and exit prettier
	#! TODO 3: store the input into a list of lists
	
    # Changed from for loop to while loop, using seperate variable to store line number and incrementing it.
	# Using i to run the while loop for number of rows.
	i = row
	line = 1
	while i > 0:
		# print which line to add
		print(f"Line {line}")

		# get the input and get rid of spaces
		temp = input("").replace(" ","")

		# check the string
		if not checkInput(temp):
			print("Invalid input, please try again")

		else:
			# Appending the list of values for a row to the main list.
			form.append(list(temp))
			i -= 1
			line += 1
	CreateSudocu(form)

# pant
def checkInput(text: str) -> bool:

	# set the charachter to search only for number or .
	letter = r"(\d|\.)"

	# try to find all matches
	matches = re.search(r"^(?:\d|\.){9}$", text)

	# if matches then return true, that the input is correct
	if matches:
		 return True

	# else return false
	return False

def CreateSudocu(form: list) -> None:
	if checkSudocu:
		print(tabulate(form, tablefmt="grid"))
	# Making a visual from the grid we will get.
	
	


# prob wuru

def checkSudocu(sudocu: list) -> bool:
	for i in row:
		for j in cols:
			if form[i][j] in form[i] or form[i][j] in form[j]

	return True


# solve it
def solve(sudocu: list) -> list:
	return []


if __name__ == "__main__":
	main()