# Enter your code here. Read input from STDIN. Print output to STDOUT

from sys import stdin


def get_result(data):
    cnt = 0
    quotient = data
    while quotient > 1:
        quotient = quotient // 2
        cnt += 1
    return 2**(cnt+1) - 1


if __name__ == '__main__':
    data = int(stdin.readline())
    result = get_result(data)
    print(result)
