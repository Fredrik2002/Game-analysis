import chess
from stockfish import Stockfish
from colors import bcolors


def get_game(path):
    started, variable = False, True
    partie = ""
    with open(path, "r") as file:
        for line in file:
            if line[0] == "1":
                print("started")
                started = True
            if started:
                if line[-1] == "\n":
                    partie+= line[:-1] + " "
                else :
                    partie +=line
    return partie

def get_eval(stockfish: Stockfish):
    eval = stockfish.get_evaluation()
    if eval['type'] == 'cp':
        if eval['value'] > 0:
            return f"+{eval['value'] / 100}"
        elif eval['value'] == 0:
            return "0.00"
        else:
            return eval['value'] / 100
    else:
        if eval['value'] > 0:
            return f"+M{eval['value']}"
        else:
            return f"-M{eval['value']}"


def eval_difference(eval_before, eval_after, white=True):
    if white:
        if eval_before['type'] != 'cp' and eval_after['type'] == 'cp':
            return 100
        elif eval_after['type'] == 'cp' and eval_before['type'] == 'cp':
            return eval_before['value'] - eval_after['value']
        else:
            return 0
    else:
        if eval_before['type'] != 'cp' and eval_after['type'] == 'cp':
            return 100 - eval_after['value']
        elif eval_after['type'] == 'cp' and eval_before['type'] == 'cp':
            return eval_after['value']-eval_before['value']
        else:
            return 0


def uci_to_algebric(stockfish: Stockfish, uci):

    value = stockfish.get_what_is_on_square(uci[:2]).value

    if stockfish.get_what_is_on_square(uci[2:]) is None:
        if value != "P" and value != "p":
            return value.upper() + uci[2:]
        else:
            return uci[2:]
    else:
        if value == "P" or value=="p":
            return uci[0] + "x" + uci[2:]
        else:
            return value.upper() + "x" + uci[2:]


def print_analyse(stockfish: Stockfish, index, move, board: chess.Board, white=True):
    best_move = stockfish.get_best_move()
    best_move_algebric = uci_to_algebric(stockfish, best_move)
    uci_moveW = board.parse_san(move)
    board.push(uci_moveW)
    stockfish.make_moves_from_current_position([best_move])
    if best_move == str(uci_moveW):
        print(f"\033[96m{index + 1}. {move}, Delta=0.00, Eval={get_eval(stockfish)} \033[0m")
    else:
        best_eval = stockfish.get_evaluation()
        stockfish.set_fen_position(board.fen())
        eval_now = stockfish.get_evaluation()
        delta = eval_difference(best_eval, eval_now, white) / 100
        if delta < 0:
            delta = "0.00"
        print(f"{get_color_code(float(delta))}{index + 1}. {move}, Delta={delta}, "
              f"Eval={get_eval(stockfish)} Best was {index+1}. {best_move_algebric} \033[0m")


def get_color_code(delta):
    if delta == 0:
        return '\033[96m'
    if delta < 0.3:
        return '\033[92m'
    if delta < 0.6 :
        return '\033[32m'
    if delta < 1:
        return '\033[93m'
    if delta < 5:
        return '\033[91m'
    return '\033[101m'


def print_palette():
    for color in dir(bcolors):
        if color[0]!="_":
            print(getattr(bcolors, color)+color+"\033[0m")
