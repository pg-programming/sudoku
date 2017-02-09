#!/usr/bin/env python

from random import randint
import sudoku_helper as sudoku
import sys
import os

scores_file = 'sudoku_scores.txt'

def list_scores(name):
    pass

def write_outcome(name, outcome):
    pass

def play_game(name, board):
    pass

def show_menu():
    # loop continually until a menu item is selected
    pass

def new_game():
    boards = sudoku.get_boards()
    board = boards[randint(0, len(boards)-1)]
    name = ""
    while not name:
        name = raw_input("What's your name? ").strip()
        if not name:
            print "Sorry, I didn't get that."
    play_game(name, board)

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
    if name != None and outcome != None:
        write_outcome(name, outcome)
        list_scores(name)
    os.system('clear')
    sys.exit()


if __name__ == '__main__':
    show_menu()
