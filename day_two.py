# day_two.py
# by Preston Hager

"""
The concept is to take a file of lines that have a
direction and magnitude and add them up to multiply
to get the final result.
"""

def part1(movements):
    movements = [tuple(m.split(' ')) for m in movements]
    # sorted_movements = sorted(movements, key=lambda x: x[0])
    down_movements = [int(movements[x][1]) for x, y in enumerate(movements) if y[0] == 'down']
    forward_movements = [int(movements[x][1]) for x, y in enumerate(movements) if y[0] == 'forward']
    up_movements = [int(movements[x][1]) for x, y in enumerate(movements) if y[0] == 'up']
    horizontal = sum(forward_movements)
    depth = sum(down_movements) - sum(up_movements)
    return horizontal * depth

def part2(movements):
    aim = 0
    depth = 0
    horizontal = 0
    movements = [tuple(m.split(' ')) for m in movements]
    for move in movements:
        if move[0] == 'up':
            aim -= int(move[1])
        elif move[0] == 'down':
            aim += int(move[1])
        elif move[0] == 'forward':
            horizontal += int(move[1])
            depth += int(move[1]) * aim
    return horizontal * depth

if __name__ == '__main__':
    import sys
    func = [part1, part2][int(sys.argv[1]) - 1]
    with open(sys.argv[2]) as f_in:
        result = func(f_in.read().strip().split('\n'))
    print(result)
