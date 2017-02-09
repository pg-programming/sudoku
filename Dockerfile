FROM python:2.7.12

COPY sudoku.py sudoku_helper.py sudoku-boards.txt /

WORKDIR /

CMD python sudoku.py
