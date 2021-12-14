# day_five.py
# by Preston Hager

def part1():
    pass

def part2():
    pass

if __name__ == '__main__':
    import sys
    func = [part1, part2][int(sys.argv[1]) - 1]
    with open(sys.argv[2]) as f_in:
        result = func(f_in.read().strip().split('\n'))
    print(result)
