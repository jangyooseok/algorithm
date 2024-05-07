# 1이 될 때까지
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정중 하나를 반복적으로 수행하려고 함
# 단 두번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하라.

import sys

n, k = map(int, sys.stdin.readline().strip().split()) # N과 K 입력

count = 0 # 계산 횟수

while n >= k: # N이 K이상인 경우 
    while n % k != 0: # N이 K로 나누어떨어지지 않으면 -1 반복
        n -= 1
        count += 1
    if n % k == 0: # N이 K로 나누어떨어지면 N = N을 K로 나눈 값
        n /= k
        count += 1

while n > 1: # 마지막으로 남은 수에 대해 1씩 빼기
    n -= 1
    count += 1

print(count)