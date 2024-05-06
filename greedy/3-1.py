# 거스름돈 동전개수 구하는 문제
import sys

money = int(sys.stdin.readline().strip()) #거슬러 줄 돈 입력

coins = [500, 100, 50, 10] #동전 종류

counts = [0]*len(coins) #거슬러줄 동전 수(500, 100, 50, 10 순서)

for i in range(len(coins)):
    counts[i] = money // coins[i] #해당 동전으로 최대한 거슬러줄 수 있는 동전 갯수
    money %= coins[i] #거슬러주고 남은 돈

print(counts)