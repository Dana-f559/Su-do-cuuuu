import sys
from helpers import solve_sudoku, checkInput
row = 3
cols = 3
form = []

#! fix when importing the input
def main():
    print("ENTER THE SUDOCU")

    # set i to row for incrementing
    i = row

    # set line to 1 
    line = 1

    # a loop for getting the input
    while i > 0:
        # print which line to add
        print(f"Line {line}")

        # get the input and get rid of spaces
        temp = input("").replace(" ", "")

        # check the string
        if not checkInput(temp):
            print("Invalid input, please try again")

        else:
            # Appending the list of values for a row to the main list.
            form.append(list(temp))
            i -= 1
            line += 1
    
    if not (solved := solve_sudoku(temp)):
        sys.exit("THE SUDOCU IS INVALID")
    else:
        print(solved)

if __name__ == "__main__":
    main()
