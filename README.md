# Game analysis w/ Stockfish

This project takes a full chess game as input and evaluate each move compared to the best one given by Stockfish

![image](https://github.com/Fredrik2002/Chess-analysis/assets/86866135/153b03da-b3ac-4789-9888-f7a9bccc63c5)

##### WARNING : This program will automatically install 3 packages via the 'pip install' command if you don't have them already :
- chess
- stockfish
- colorama

## Usage
1. Go to *main.py*, line 8, and enter the path of your Stockfish engine in `path=''`
(Warning : The path needs to be passed with forward slash (/) and not blackslash (\\), e.g.
C:/Users/XXXX/Desktop/stockfish-windows-x86-64-avx2/stockfish/stockfish-windows-x86-64-avx2)
2. Paste the PGN of your game in the game.txt file (or the game itself starting by 1.e4 e5 2.Cf3 ...)
3. Run main.py
4. Type 0 or 1 in the console if you want to analyse white or black side <br><br>

## Improvements / Contributions / Work in Progress :
- Calculate a % accuracy at the end of the game
- Optimizations in *utils.py*
- Any other idea are welcome !

