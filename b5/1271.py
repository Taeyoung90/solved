# 통과
import sys

input_raw = sys.stdin.readline().split() # input()보다 속도가 빠름

n = int(input_raw[0])
m = int(input_raw[1])

answer1 = n//m
answer2 = n%m
    
print(answer1)
print(answer2)

    