from utils import *
from math import sqrt


init()
partie = get_game("game.txt")
DEPTH = 12 # you can reduce if the program takes too much time/CPU
board = chess.Board()
stockfish = Stockfish(path="C:/Users/calve/Downloads/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2", depth=DEPTH) #YOUR STOCKFISH PATH HERE
partie = partie.split('.')[1:]
v = [0]

def print_end(index):
    print()
    print(f"Variance : {round(v[0]/index, 2)}")
    print(f"Standard deviation : {round(sqrt(v[0]/index), 2)}")

def white():
    try:    
        for index, move in enumerate(partie):
            move = (move[1:].split(' '))
            print_analyse(stockfish, index, move[0], board, v)
            uci_moveB = board.parse_san(move[1])
            board.push(uci_moveB)
            stockfish.make_moves_from_current_position([str(uci_moveB)])
    except :
        print_end(index+1)
        return
    print_end(index)


def black():
    try:
        for index, move in enumerate(partie):
            
            move = (move[1:].split(' '))

            uci_moveW = board.parse_san(move[0])
            board.push(uci_moveW)
            stockfish.make_moves_from_current_position([str(uci_moveW)])
            print_analyse(stockfish, index, move[1], board, v, white=False)
            
    except :
        print_end(index)
    print_end(index+1)
    


variable = input("Which side do you want to analyse ? 0 = White |  1 = Black\n")
while variable != "0" and variable != "1":
    variable = input("0 = White |  1 = Black\n")

if variable == "0":
    white()
else:
    black()
