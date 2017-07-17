# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

from copy import deepcopy

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sorted_lines(piece1,piece2):
    if piece1==piece2:
        return True
    else:
        return False
        
def check_horizontal(puzzle):
    attempt=deepcopy(puzzle) #because lists mutate, we need to only work with the clone, not the original
    for piece in attempt:
        piece.sort() #sort every horizontal line
        index=0
        for part in range(1,piece[-1]): #each line should range from 1 to the maximum number in the line
            if part==piece[index]: #check each number against what it should be for proper sudoku form
                index+=1
                continue
            else:
                return False #failed the test
    n=piece[-1] #the highest number in the horizontal line should be the size of the square
    i=0
    while i<n and check_sorted_lines(attempt[i-1],attempt[i]): #check if the last and the current horizontal line are the same
        i+=1
    if i==n: #if (after sorting) the number of matching horizontal lines is the same as the size of the square
        return True #passed the test
    else:
        return False #failed the test
        
def check_vertical(puzzle):
    attempt=deepcopy(puzzle)
    transversion=[]
    index=0
    while index<len(attempt):
        column=[]
        for item in attempt:
            column.append(item[index])
        index+=1
        transversion.append(column)
    return check_horizontal(transversion)
        

def check_sudoku(puzzle):
    try:
        if check_horizontal(puzzle) and check_vertical(puzzle): #we have to pass both tests here
            return True
        else:
            return False
    except:
        return False

print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False