from utils import *

stockfish = Stockfish(
    path="stockfish/stockfish-windows-x86-64-avx2.exe", depth=20)

started, variable = False, True
partie = ""
with open("game.txt", "r") as file:
    for line in file:
        if line[0] == "1":
            print("started")
            started = True
        if started:
            if line[-1] == "\n":
                partie+= line[:-1] + " "
            else :
                partie +=line

print(partie)