class Board:
    def __init__(self):
        self.board = {
                "1": " ", "2": " ", "3": " ",
                "4": " ", "5": " ", "6": " ",
                "7": " ", "8": " ", "9": " "}

    def printBoard(self):
        print(self.board["1"] + "|" + self.board["2"] + "|" + self.board["3"])
        print("-+-+-")
        print(self.board["4"] + "|" + self.board["5"] + "|" + self.board["6"])
        print("-+-+-")
        print(self.board["7"] + "|" + self.board["8"] + "|" + self.board["9"])

    def isValidMove(self, position):
        if self.board[position] == " ":
            return True
        return False

    def changeBoard(self, position, type):
        if self.isValidMove(position):
            self.board[position] = type
            return self.board
        return None

    def isWinner(self, player):
        if self.board["1"] == player.type and self.board["2"] == player.type and self.board["3"] == player.type or \
        self.board["4"] == player.type and self.board["5"] == player.type and self.board["6"] == player.type or \
        self.board["7"] == player.type and self.board["8"] == player.type and self.board["9"] == player.type or \
        self.board["1"] == player.type and self.board["4"] == player.type and self.board["7"] == player.type or \
        self.board["2"] == player.type and self.board["5"] == player.type and self.board["8"] == player.type or \
        self.board["3"] == player.type and self.board["6"] == player.type and self.board["9"] == player.type or \
        self.board["1"] == player.type and self.board["5"] == player.type and self.board["9"] == player.type or \
        self.board["7"] == player.type and self.board["5"] == player.type and self.board["3"] == player.type:
            return True
        return False


class Player:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "Player {}".format(self.type)


class Game:
    def __init__(self):
        self.firstPlayer = Player("X")
        self.secondPlayer = Player("O")
        self.board = Board()

    def printValidEntries(self):
        print("""
            1 | 2 | 3
            4 | 5 | 6 
            7 | 8 | 9 """)

    def printingBoard(self):
        self.board.printBoard()

    def changeTurn(self, player):
        if player == self.firstPlayer:
            return self.secondPlayer
        else:
            return self.firstPlayer

    def wonGame(self, player):
        return self.board.isWinner(player)

    def modifyBoard(self, position, type):
        if self.board.changeBoard(position, type) is not None:
            return self.board.changeBoard(position, type)
        else:
            position = input("Not available position. Please, try again: ")
            return self.board.changeBoard(position, type)


def play():
    game = Game()
    game.printValidEntries()
    player = game.firstPlayer
    number = 9
    while number > 0:
        number -= 1
        game.printingBoard()
        position = input("{} turn, what's your move? ".format(player))
        game.modifyBoard(position, player.type)
        if game.wonGame(player):
            print("{} is the Winner!".format(player))
            break
        else:
            player = game.changeTurn(player)
    if number == 0:
        print("Game over! It's a tie!")

play()