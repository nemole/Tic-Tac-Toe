class Board:
    def __init__(self, grid = [[0,0,0],[0,0,0],[0,0,0]]):
        self.grid = grid

    def reset_board(self):
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]

    def print_board(self):
        print("  ┌───┬───┬───┐")
        print("3", end = "")
        for x in range(3):
            print(" │ " + self.convert(self.grid[0][x]), end = "")
        print(" │")
        print("  ├───┼───┼───┤")
        print("2", end = "")
        for x in range(3):
            print(" │ " + self.convert(self.grid[1][x]), end = "")
        print(" │")
        print("  ├───┼───┼───┤")
        print("1", end = "")
        for x in range(3):
            print(" │ " + self.convert(self.grid[2][x]), end = "")
        print(" │")
        print("  └───┴───┴───┘")
        print("    A   B   C")

    def check_winner(self, shape):
        if self.grid[0][0] == shape and self.grid[0][1] == shape and self.grid[0][2] == shape:
            self.grid[0][0] = self.grid[0][1] = self.grid[0][2] = shape + 2
            return True
        if self.grid[1][0] == shape and self.grid[1][1] == shape and self.grid[1][2] == shape:
            self.grid[1][0] = self.grid[1][1] = self.grid[1][2] = shape + 2
            return True
        if self.grid[2][0] == shape and self.grid[2][1] == shape and self.grid[2][2] == shape:
            self.grid[2][0] = self.grid[2][1] = self.grid[2][2] = shape + 2
            return True
        if self.grid[0][0] == shape and self.grid[1][0] == shape and self.grid[2][0] == shape:
            self.grid[0][0] = self.grid[1][0] = self.grid[2][0] = shape + 2
            return True
        if self.grid[0][1] == shape and self.grid[1][1] == shape and self.grid[2][1] == shape:
            self.grid[0][1] = self.grid[1][1] = self.grid[2][1] = shape + 2
            return True
        if self.grid[0][2] == shape and self.grid[1][2] == shape and self.grid[2][2] == shape:
            self.grid[0][2] = self.grid[1][2] = self.grid[2][2] = shape + 2
            return True
        if self.grid[0][0] == shape and self.grid[1][1] == shape and self.grid[2][2] == shape:
            self.grid[0][0] = self.grid[1][1] = self.grid[2][2] = shape + 2
            return True
        if self.grid[0][2] == shape and self.grid[1][1] == shape and self.grid[2][0] == shape:
            self.grid[0][2] = self.grid[1][1] = self.grid[2][0] = shape + 2
            return True
        return False

    def check_end(self):
        for x in self.grid:
            for y in x:
                if y == 0:
                    return False
        return True

    def convert(self, x):
        if x == 0:
            return " "
        if x == 1:
            return "✖"
        if x == 2:
            return "⚬"
        if x == 3:
            return "\033[32m✖\033[39m"
        if x == 4:
            return "\033[32m⚬\033[39m"

class Player:
    def __init__(self, marker, isHuman):
        self.mark = marker
        self.isHuman = isHuman
    



def main():
    turn = 1
    board = Board()
    print("\n" + "-"*7, end = "")
    print("TIC TAC TOE", end = "")
    print("-"*7 + '\n')
    while True:
        if turn == 1:
            print("It is ✖'s turn to play")
        else:
            print("It is ⚬'s turn to play")
        
        board.print_board()

        coord = input("Enter Coordinates to play: ")
        try:
            letter = ord(coord[0].upper()) - 65
            number = (int(coord[1]) - 3) * -1

            if number < 0 or letter < 0:
                raise ValueError("Negative index")
                
            if board.grid[number][letter] == 0:
                board.grid[number][letter] = turn
                if board.check_winner(turn):
                    board.print_board()
                    break
                if board.check_end():
                    board.print_board()
                    turn = 3
                    break
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
            else:
                print("\n\033[31mThat spot has already been filled\033[39m\n")
        except:
            print("\n\033[31mThat is not a valid coordinate\033[39m\n")
    if turn == 1:
        print("✖ Wins!")
    elif turn == 2:
        print("⚬ Wins!")
    else:
        print("Tie Game")
    
if __name__ == "__main__":
    main()
