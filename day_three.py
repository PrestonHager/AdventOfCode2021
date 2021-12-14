# day_three.py
# by Preston Hager

from copy import copy

def get_letter(num, report, default='1'):
    letters = [s[num] for s in report]
    if letters.count('1') == letters.count('0'):
        return default
    return max(set(letters), key=letters.count)

def part1(report):
    line_len = len(report[0])
    gamma_string = "0b" + ''.join([get_letter(n, report) for n in range(line_len)])
    gamma = int(gamma_string, 2)
    epsilon = (~gamma & 2**line_len-1)
    return gamma * epsilon

def part2(report):
    o2_nums = copy(report)
    co2_nums = copy(report)
    bit_num = 0
    while len(o2_nums) > 1:
        most_common = get_letter(bit_num, o2_nums)
        o2_nums = [n for n in o2_nums if n[bit_num] == most_common]
        bit_num += 1
    bit_num = 0
    while len(co2_nums) > 1:
        least_common = ['1', '0'][int(get_letter(bit_num, co2_nums))]
        co2_nums = [n for n in co2_nums if n[bit_num] == least_common]
        bit_num += 1
    return int("0b" + o2_nums[0], 2) * int("0b" + co2_nums[0], 2)

if __name__ == '__main__':
    import sys
    func = [part1, part2][int(sys.argv[1]) - 1]
    with open(sys.argv[2]) as f_in:
        result = func(f_in.read().strip().split('\n'))
    print(result)
