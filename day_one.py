# dayone.py
# by Preston Hager

def main(depths):
    increased = 0
    previous = -1
    for depth in depths:
        if previous < int(depth):
            increased += 1
        previous = int(depth)
    return increased - 1

def main2(measurements):
    windows = [measurements[i:i+3] for i in range(len(measurements))]
    sums = [sum([int(n) for n in w]) for w in windows]
    increased = 0
    previous = -1
    for s in sums:
        if previous < s:
            increased += 1
        previous = s
    return increased - 1

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f_in:
        increased = main2(f_in.read().strip().split('\n'))
    print(increased)
