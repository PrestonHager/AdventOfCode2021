# day_four.py
# by Preston Hager

from copy import copy

def flatten(board):
    return [r for sub in board for r in sub]

def rotate(board):
    return list(zip(*reversed(board)))

def _check_win(_board):
    for row in _board:
        if len(set(row)) == 1:
            return True
    return False

def board_wins(board):
    board_rotated = rotate(board)
    if _check_win(board):
        return (True, 'row')
    if _check_win(board_rotated):
        return (True, 'col')
    return (False, 'none')

def parse(bingo_input):
    # parse the bingo input form the file
    bingo_numbers = bingo_input[0].split(',')
    bingo_input = bingo_input[2:]
    boards = []
    board_index = 0
    for line in bingo_input:
        if line == '':
            board_index += 1
        else:
            if len(boards) <= board_index:
                boards.append([])
            board = boards[board_index]
            board.append(line.split())
    return [bingo_numbers, boards]

def emulate(bingo_numbers, boards, to="WINNER"):
    # iterate through bingo numbers
    winner = (-1, 'none')
    boards_won = 0
    loser = (-1, 'none')
    final_number = 0
    for num in bingo_numbers:
        board_index = 0
        for board in boards:
            if boards[board_index][-1] == "W":
                board_index += 1
                continue
            flattened = flatten(board)
            replaced = ['T' if el == str(num) else el for el in flattened]
            board = [[replaced[i*5+j] for j in range(5)] for i in range(5)]
            boards[board_index] = board
            winnings = board_wins(board)
            if winnings[0]:
                boards_won += 1
                boards[board_index].append("W")
                if boards_won == 1:
                    winner = (board_index, winnings[1])
                elif boards_won == len(boards):
                    loser = (board_index, winnings[1])
                    break
                if to == "WINNER":
                    break
            board_index += 1
        if winner[0] > -1 and to == "WINNER":
            break
        if loser[0] > -1:
            break
    return [winner, loser, num]

def score(winning_board, last_call):
    # figure out which row it was
    winning_row = -1
    for r in range(len(winning_board)):
        if len(set(winning_board[r])) == 1:
            winning_row = r
            break
    # calculate sum of all unmarked numbers
    unmarked = sum([0 if n == 'T' else int(n) for n in flatten(winning_board)])
    return unmarked * int(last_call)

def part1(bingo_input):
    bingo_numbers, boards = parse(bingo_input)
    winner, loser, last_call = emulate(bingo_numbers, boards)
    # calculate the winner's score
    winning_board = boards[winner[0]]
    winning_board.pop()
    if winner[1] == 'col':
        winning_board = rotate(winning_board)
    return score(winning_board, last_call)

def part2(bingo_input):
    bingo_numbers, boards = parse(bingo_input)
    winner, loser, last_call = emulate(bingo_numbers, boards, to="LOSER")
    # calculate the winner's score
    losing_board = boards[loser[0]]
    losing_board.pop()
    if loser[1] == 'col':
        losing_board = rotate(losing_board)
    # figure out which row it was
    return score(losing_board, last_call)

if __name__ == '__main__':
    import sys
    func = [part1, part2][int(sys.argv[1]) - 1]
    with open(sys.argv[2]) as f_in:
        result = func(f_in.read().strip().split('\n'))
    print(result)
