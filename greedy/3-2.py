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

while m > 0: # 더할 횟수가 남지 않을 때 까지
    for i in range(k): # 가장 큰 수를 최대로 연속해서 더할 수 있을때까지
        result += first
        m -= 1
    if m == 0:
        break
    else: # 가장 큰 수의 합이 끝난 후 두번째로 큰 수를 한번 더함 
        result += second
        m -= 1

print(result)