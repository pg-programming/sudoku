#!/usr/bin/env python

from random import randint
import sudoku_helper as sudoku
import sys
import os

scores_file = 'sudoku_scores.txt'


def list_scores(name):
    with open(scores_file, 'r') as f:
        results = parse_results(f.readlines())
    if name not in results:
        input("There are no results for %s..." % name)
        return
    wins = results[name][0]
    losses = results[name][1]
    input("\n%s's record is %d wins and %d losses..." % (name, wins, losses))


def write_outcome(name, outcome):
    with open(scores_file, 'a') as f:
        f.write("%s %s\n" % (name, outcome))


def parse_results(results):
    results_dict = {}
    for result in results:
        parts = result.split()
        if len(parts) > 2:
            raise Exception("the results file has a bad format")
        name = parts[0]
        outcome = parts[1]
        if name not in results_dict:
            results_dict[name] = (0, 0)
        if outcome == 'w':
            results_dict[name] = (results_dict[name][0]+1, results_dict[name][1])
        elif outcome == 'l':
            results_dict[name] = (results_dict[name][0], results_dict[name][1]+1)
        else:
            raise Exception("I didn't recognize the outcome")
    return results_dict


def quit(name=None, outcome=None):
    if name is not None and outcome is not None:
        write_outcome(name, outcome)
        list_scores(name)
    os.system('clear')
    sys.exit()


def parse_input(input):
    if len(input) != 4:
        return None, None, None
    return input[0], input[1], input[3]


def play_game(name, board):
    while True:
        os.system('clear')
        sudoku.print_sudoku()
        sudoku.print_board(board)
        print("\nSelect a position and value (e.g. A4 7) or enter q to quit")
        result = input("> ")
        if result == 'q':
            quit(name, 'l')
        col, row, val = parse_input(result)
        if not col or not row or not val:
            input("Invalid format. You must enter a column, row, separator character and value in that order...")
            continue
        new_board = sudoku.update_board(board, col, row, val)
        if not new_board:
            input("Unable to update board at %s%s with %s...".format(
                col.upper(),
                row,
                val
            ))
            continue
        board = new_board
        if sudoku.detect_win(board):
            sudoku.print_victory()
            quit(name, 'w')


def new_game():
    boards = sudoku.get_boards()
    board = boards[randint(0, len(boards)-1)]
    name = ""
    while not name:
        name = input("What's your name? ").strip()
        if not name:
            print("Sorry, I didn't get that.")
    play_game(name, board)


def show_menu():
    while True:
        os.system('clear')
        sudoku.print_sudoku()
        print("(n)ew game\n(l)ist scores\n(q)uit\n")
        option = sudoku.get_ch()
        if option == 'q':
            quit()
        elif option == 'n':
            new_game()
        elif option == 'l':
            name = input("Whose scores do you want to see? ")
            list_scores(name)
        else:
            input("I didn't recognize that option...")


if __name__ == '__main__':
    show_menu()
