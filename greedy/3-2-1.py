# 큰수의 법칙
# 다양한 수들로 이루어진 배열이 있을 때
# 주어진 수들을 M번 더하여 가장 큰 수를 만드는 문제
# 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없음

# 배열의크기 N, 숫자가 더해지는 횟수 M, 그리고 K 가 주어질 때
# 결과인 큰 수를 출력할 것

# 입력 값은 순서대로 N, M, K 그리고 숫자배열
# 단 K <= M

import sys

n, m, k = map(int,sys.stdin.readline().strip().split()) # N, M ,K값 입력

data = list(map(int,sys.stdin.readline().strip().split())) # 수 배열 입력

data.sort() # 배열 정렬

first = data[-1] # 배열 중 가장 큰 값
second = data[-2] # 배열 중 두번째로 큰 값

result = 0 # 결과 값(합)을 저장할 변수

# ((가장 큰 수 * K) + 두번째로 큰 수) 가 반복되어 더해지는 규칙이 있음
# count는 가장 큰 수가 더해지는 횟수
# m // (k+1)은 규칙이 있는 수열의 반복되는 횟수
# m % (k+1)은 m이 k+1로 나누어 떨어지지 않는 경우 나머지로 그만큼 가장 큰 수가 추가로 더해짐
count = (m // (k+1)) * k + (m % (k+1))

result = first * count + (m - count) * second

print(result)