"""
Battleship.py

This is a simplified version of Battleship where users guess a grid coordinate to find the single ship. 
"""
import random
import os

#Grid size is fixed
GRID_ROWS = 5
GRID_COLS = 5

#Display characters to represent game elements
CHAR_OPEN = 'O'
CHAR_MISS = 'X'
CHAR_SHIP = 'S'

def read_int(prompt: str, min: int = 1, max: int = 5) -> int:
    """Takes an input from user and ensures it's an integer"""
    while True: 
        line = input(prompt)
        try: 
            value = int(line)
            if min <= value <= max:
                return value
            else:
                print(f"Input must be between {min} and {max}.")
        except ValueError:
            print("Input must be a number.")

def setup_grid(nRows: int, nCols: int) -> list:
    """Creates a 2D list of lists"""
    grid = [ ["O"]*nRows for i in range(nCols)]                                #Empty grid
    grid[random.randrange(0,nRows)][random.randrange(0,nCols)] = CHAR_SHIP     #Place the ship
    return grid

def print_grid(grid: list, replaceChar: str = None, replaceWith: str = None) -> None:
    """Prints the grid to the console"""
    print('\n'.join(map(''.join, [[col if col != replaceChar else replaceWith for col in row] for row in grid])))

def print_winner(playerID: int) -> None:
    """Displays the winner"""
    print(f"Player {playerID} has won! Congratulations!")

def make_guess(grid: list) -> bool:
    """Reads the guess row and column from the player"""
    
    while True: 
        guessRow = read_int("Guess Row: ", 1, GRID_ROWS) - 1
        guessCol = read_int("Guess Col: ", 1, GRID_COLS) - 1
        
        if grid[guessRow][guessCol] == CHAR_OPEN:
            grid[guessRow][guessCol] = CHAR_MISS
            return False
        elif grid[guessRow][guessCol] == CHAR_SHIP:
            return True
        else: 
            print("That's already been guessed! Try again.")
    
def game_loop(nPlayers, grid) -> int:
    """The main game loop"""
    
    while True:
        for iPlayer in range(1,nPlayers + 1):
            print_grid(grid,CHAR_SHIP,CHAR_OPEN)
            print(f"Player {iPlayer} is up!")
            if make_guess(iPlayer, grid): return iPlayer

def main() -> None: 
    """Initialize execution"""
    #Get number of players
    nPlayers = read_int("Enter the number of players: ")
    
    #Create grid
    grid = setup_grid(GRID_ROWS, GRID_COLS)
    
    #Play the game
    winnerID = game_loop(nPlayers, grid)
    
    #Print winner
    os.system("clear")
    print_grid(grid)
    print_winner(winnerID)

if __name__ == "__main__":
    main()
