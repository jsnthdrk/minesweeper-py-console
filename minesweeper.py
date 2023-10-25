# I spent 2 weeks on this, made by jsnthdrk on github, enjoy!
# Your plan of action:
# 1- you need to make an empty field, a 2d list
# 2- afterwards, we use the random function to generate the mines across the field
# 3- then, we plan ahead, and hide our mines inside the board
# 4- we show our "real" field, we need a temporary solution field and then our playing field
# 5- now, we do the game loop with win/lose conditions, error handling


import random

def mainMS():
    # 1
    def makeField(width, height, num_mines):
        # empty field
        field = [[" - " for i in range(width)] for j in range(height)]
        
        # 2- lays mines
        for i in range(num_mines):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            while field[y][x] == "*":
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
            field[y][x] = "*"
        
        # 3- hides mines
        for y in range(height):
            for x in range(width):
                if field[y][x] != "*":
                    count = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if 0 <= x + dx < width and 0 <= y + dy < height and field[y + dy][x + dx] == "*":
                                count += 1
                    if count > 0:
                        field[y][x] = " " + str(count) + " "

        return field
    # 4- shows field
    def showsRealField(board):
        width = len(board[0])
        height = len(board)
        # do grid
            # upmost part of grid
        print("\n     ", end="")
        for col in range(width):
            print(f" {( 0 + col)}   ", end="")
        print("\n    +" + "----+" * width)
        
        # remainder of the grid
        for row in range(height):
            print(f"{row:2d}  |", end="")
            for col in range(width):
                value = board[row][col]
                print(f"{value} |", end="")
            print("\n    +" + "----+" * width)
    # 5 - we make our main game loop, where the brainstorming comes in, we have to show the mines after losing, we need to make our win/lose conditions and we do our error handling
    # main loop
    def main():
        width = 10
        height = 10
        num_minas = 1

        field = showsRealField(width, height, num_minas)
        board = [["   " for i in range(width)] for j in range(height)]
        # game loop
        while True:
            # input
            makeField(board)
            x_input = input("Enter a column (0-9) or 'q' to exit: ")
            if x_input == 'q':
                print("Left the game.")
                break

            # error handling, prevents the input being empty (enter) or the row or col to be larger than 9, negative number or letter
            if x_input.isnumeric():
                x = int(x_input)
                if 0 <= x < width:
                    y_input = input("Enter a column (0-9) or 'q' to exit: ")
                    if y_input.isnumeric():
                        y = int(y_input)
                        if 0 <= y < height:
                            # perde
                            if field[y][x] == "*":
                                print("You hit a mine, game over.")
                                # shows mines position after losing
                                for i in range(height):
                                    for j in range(width):
                                        if field[i][j] == "*":
                                            board[i][j] = " * "
                                makeField(board)
                                break
                            else:
                                board[y][x] = field[y][x]

                            # win condition
                            if all(board[i][j] != "   " or field[i][j] == "*" for i in range(height) for j in range(width)):
                                makeField(board)
                                print("You win!")
                                break
                        else:
                            print("Column out of bounds.")
                    else:
                        print("Invalid input, please enter a column (0-9 or 'q' to exit: ")
                else:
                    print("Row out of bounds")
            else:
                print("Invalid input, please enter a column (0-9 or 'q' to exit: ")
        # ^^^ your error messages
    if __name__ == "__main__": # good practises
        main()

mainMS() # your main function, in my case I used this game in a bundle of games with a menu, best to keep it within a main function that has all of your game functions and main game loop nested.
