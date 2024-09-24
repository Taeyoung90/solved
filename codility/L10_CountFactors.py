# 100

"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.
D는 N 의 약수 ,M도 약수
For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2024 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

약수 개수 찾는 알고리즘
"""
import math
def solution(N):
    check_list = list(range(1, int(math.sqrt(N))+1))
    factors = []

    for i in check_list:
        if N % i == 0:
            factors.append(i)
            if i == N//i:
                break
            factors.append(N//i)
        
    return len(factors)

if __name__ == "__main__":
    A = 100

    print(solution(A))