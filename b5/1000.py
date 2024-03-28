import sys

# def solution(n,m):
#     answer =0
#     return answer


if __name__ == '__main__':
    # input_ = input().split()
    input_raw = sys.stdin.readline().split() # input()보다 속도가 빠름
    
    print(sum(map(int,input_raw)))