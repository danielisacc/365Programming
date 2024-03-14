"""
Program to Create a Tic-Tac-Toe game as an interview question...

problem statement:
ou need to create a Python program that allows two players to play a game of tic-tac-toe.
The game should be text-based, with the board displayed after each move.
The program should handle input validation and determine the winner or if the game ends in a draw.

requirements:
1    The game should be played on a 3x3 grid.
2    Games should take turns, marking the spaces with 'X' and 'O'.
3    The game should end when one player has three of their marks in a row (horizontally, vertically, or diagonally) or when the board is full (resulting in a draw).
4    The program should display the current state of the board after each move.
5    Input validation should be implemented to ensure that players enter valid moves (i.e., within the range 1-9 and in an empty space).

Additional Challenges:
1    Implement error handling for invalid inputs (e.g., non-integer inputs, out-of-range inputs, already occupied spaces).
2    Allow players to play again after a game has ended.
3    Add a feature to display the total score (number of wins for each player) across multiple games.

"""

class Board:

    board_matrix = [[1,2,3],
                    [4,5,6],
                    [7,8,9]]
    
    def print_board(self):
        print("Tic-Tac-Toe\n")
        row = 0
        for i in range(5):
            if i % 2 == 0:
                print(f" {Board.board_matrix[row][0]} | {Board.board_matrix[row][1]} | {Board.board_matrix[row][2]}")
                row += 1
            else: print(" ---------")
        print("\n")

class Win_States:
    win_state = False
    winner = None
    def __init__(self, board: Board, turn) -> None:
        super().__init__()
        self.board = board  

        win_states = [["","",""],["","",""],["","",""]]

        for x in range(0,3):
            if self.board.board_matrix[x] == [turn,turn,turn]: 
                Win_States.win_state = True
                Win_States.winner = turn
            win_states[0][x] = self.board.board_matrix[x][x]
            win_states[1][x] = self.board.board_matrix[x][2-x]

            for y in range(0,3):
                win_states[2][y] = self.board.board_matrix[y][x]
            
            if win_states[2] == [turn,turn,turn]:
                Win_States.win_state = True
                Win_States.winner = turn
        if win_states[0] == [turn,turn,turn]:
            Win_States.win_state = True
            Win_States.winner = turn
        if win_states[1] == [turn,turn,turn]:
            Win_States.win_state = True
            Win_States.winner = turn
                
        

class Game:

    gamestate = True

    def __init__(self, player1_piece:str = "X", player2_piece:str = "O") -> None:
        self.player1 = player1_piece
        self.player2 = player2_piece

        self.board = Board()
        self.board.print_board()


    def place_piece(self):
        selected = []
        turn = self.player1
        while Game.gamestate:
            try:
                selection = int(input(f"player {turn} select a coordinate to place your piece : "))
                if selection > 9 or selection < 0:
                    raise ValueError()
                if selection in selected:
                    raise ValueError()
            except ValueError:
                print("Input Invalid! Please input the Integer on the Grid you would like to place a piece on...\n")
                if selection > 9 or selection < 0: print("The value entered is out of range! Enter an integer between 1 and 9!\n")
                if selection in selected: print("That spot is taken! Try another spot\n")
                
            else:
                selected.append(selection)
                

                if selection == 0:
                    Game.gamestate = False

                row = -(selection // -3)
                col = 2 - ((row*3) - selection)
                row = row - 1

                self.board.board_matrix[row][col] = turn

                win_state = Win_States(self.board, turn)

                if Win_States.win_state:
                    Game.gamestate = False
                    print(f"\n  {turn} Wins!")

                if turn == self.player1: turn = self.player2
                else: turn = self.player1
            if len(selected) == 9: 
                Game.gamestate = False
                print("Tied Game!")
            self.board.print_board()
        

game = Game()

game.place_piece()

