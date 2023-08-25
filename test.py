import chess
import inspect

board = chess.Board()
move = chess.Move.from_uci("e2e4")
print(board.san(move))

callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
frame = callerframerecord[0]
info = inspect.getframeinfo(frame)
print(info.filename)                      # __FILE__     -> Test.py
print(info.function)                      # __FUNCTION__ -> Main
print(info.lineno)