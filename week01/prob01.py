import math


def solution(change):
    count_100 = math.floor(change / 100)
    print(count_100)
    change %= 100
    count_50 = math.floor(change / 50)
    print(count_50)
    change %= 50
    count_10 = math.floor(change / 10)
    print(count_10)
    change %= 10
    return count_100 + count_50 + count_10


# test
answer = solution(160)
print(answer)
