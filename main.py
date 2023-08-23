
from utils import *

partie = get_game("game.txt")

couleur = 0
DEPTH = 18
board = chess.Board()
stockfish = Stockfish(
    path="stockfish/stockfish-windows-x86-64-avx2.exe", depth=DEPTH)
print(stockfish.get_stockfish_major_version())
partie = partie.split('.')[1:]


def white():
    for index, move in enumerate(partie):
        move = (move[1:].split(' '))

        print_analyse(stockfish, index, move[0], board)

        uci_moveB = board.parse_san(move[1])
        board.push(uci_moveB)
        stockfish.make_moves_from_current_position([str(uci_moveB)])


def black():
    for index, move in enumerate(partie):
        move = (move[1:].split(' '))

        uci_moveW = board.parse_san(move[0])
        board.push(uci_moveW)
        stockfish.make_moves_from_current_position([str(uci_moveW)])

        print_analyse(stockfish, index, move[1], board, False)


variable = input("Which side do you want to analyse ? 0 = White |  1 = Black")
while variable != "0" and variable != "1":
    variable = input("0 = White |  1 = Black")

if variable == "0":
    white()
else:
    black()
