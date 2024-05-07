# 숫자 카드 게임
# 숫자가 쓰인 카드들이 N x M 형태로 놓여있음.
# N은 행, M은 열을 의미하며 먼저 뽑고자 하는 행을 선택한다
# 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함.
# 따라서 처음에 카드를 골라낼 행을 선택할 때,
# 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

import sys

# 행, 열 입력
n, m = map(int, sys.stdin.readline().strip().split())

result = 0 # 결과 값을 저장할 변수

for _ in range(n): # 행만큼 반복
    data = list(map(int, sys.stdin.readline().strip().split())) # 열에 해당하는 값 입력
    minVal = min(data) # 해당 열의 최소값
    result = max(minVal,result) # 모든 행을 돌면서 각 행의 최소값중 최대값을 저장

print(result)