import sys
import re
from tabulate import tabulate

#These are the global constants for the size of sudoku
row = 9
cols = 9

def main():
	print("ENTER THE SUDOCU")
	form = [] #This is the Sudoku
	#DONE TODO 1: reask the user if the input is not correct
	#! TODO 2: except keybord interuption, and exit prettier
	#! TODO 3: store the input into a list of lists
	
    # Changed from for loop to while loop, using seperate variable to store line number and incrementing it.
	# Using i to run the while loop for number of rows.
	i = row # Putting i = row because I am using it for while loop with decrement, and dont wanna affect the global variable
	line = 1 #This is used solely for the purpose of denoting the position of line.
	while i > 0: #This will run the loop until row times, getting input for each row
		# print which line to add
		print(f"Line {line}")

		# get the input and get rid of spaces
		temp = input("").replace(" ","")

		# check the string
		if not checkInput(temp):
			print("Invalid input, please try again")

		else:
			# Appending the list of values for a row to the Sudoku{form}.
			form.append(list(temp))
			i -= 1 #This row input valid so decrementing
			line += 1 #This row accepted so incrementing for it to print line {n} where n is next line no.
	CreateSudocu(form) #This is for visual display of grid.

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
	# for i in row:
	# 	for j in cols:
	# 		if form[i][j] in form[i] or form[i][j] in form[j]

	return True


# solve it
def solve(sudocu: list) -> list:
	return []


if __name__ == "__main__":
	main()