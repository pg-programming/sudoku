import sys
import tty
import termios

def get_board(lines):
    board = []
    for i in range(9):
        line = []
        for char in lines[i]:
            if char == '-':
                char = '0'
            line.append(char)
        board.append(line)
    return board, len(lines)+10

def print_board(board):
    print "    A B C   D E F   G H I"
    print "  ._______________________."
    for i, line in enumerate(board):
        print "%d |" % i,
        for j, char in enumerate(line):
            print "%s" % ('-' if char == '0' else char),
            if (j+1) % 3 == 0:
                print "|",
        print
        if (i+1) % 3 == 0:
            print "  |_______|_______|_______|"

def get_boards():
    with open('sudoku-boards.txt', 'r') as f:
        lines = [ l.strip() for l in f.readlines() if l.strip() ]
    boards = []
    cur_line = 0
    while cur_line < len(lines):
        line = lines[cur_line]
        if line.startswith('#'):
            cur_line += 1
            continue
        if '%board%' in line: 
            board, cur_line = get_board(lines[cur_line+1:])
            boards.append(board)
        else:
            cur_line += 1
    return boards

def get_ch(message=None):
    if message:
        print message,
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def valid_line(line):
    for i in range(1, 10):
        if str(i) not in line:
            return False
    return True

def valid_column(board, index):
    col = []
    for i in range(9):
        col.append(board[i][index])
    return valid_line(col)

def valid_square(board, index):
    square = []
    row_start = 0
    if index > 2 and index < 6:
        row_start = 3
    elif index > 5 and index < 9:
        row_start = 6
    for i in range(row_start, row_start+3):
        col_start = (3*index) % 9
        for j in range(col_start, col_start+3):
            square.append(board[i][j])
    return valid_line(square)

def detect_win(board):
    for i in range(9):
        if not valid_line(board[i]) or not valid_column(board, i) or not valid_square(board, i):
            return False
    return True

def update_board(board, col, row, val):
    def valid(val):
        return val > -1 and val < 10
    if len(col) != 1 or len(row) != 1 or len(val) != 1:
        return None
    try:
        col = ord(col.upper()[0]) - 65
        row = int(row)
        if not valid(col) or not valid(row) or not valid(int(val)):
            return None
        board[row][col] = val
        return board
    except:
        return None

def print_sudoku():
    print """
   _____           _       _          
  / ____|         | |     | |         
 | (___  _   _  __| | ___ | | ___   _ 
  \___ \| | | |/ _` |/ _ \| |/ / | | |
  ____) | |_| | (_| | (_) |   <| |_| |
 |_____/ \__,_|\__,_|\___/|_|\_\\__,_|
 """

                                      

def print_victory():
    print """
 __      ___      _                   _ 
 \ \    / (_)    | |                 | |
  \ \  / / _  ___| |_ ___  _ __ _   _| |
   \ \/ / | |/ __| __/ _ \| '__| | | | |
    \  /  | | (__| || (_) | |  | |_| |_|
     \/   |_|\___|\__\___/|_|   \__, (_)
                                 __/ |  
                                |___/   
"""
                                                          
