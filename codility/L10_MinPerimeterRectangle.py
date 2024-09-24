#
# 넓이가 주어질때 최소인 둘레값
'''
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B). 둘레구하기

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

class Solution { public int solution(int N); }

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].

'''
# 둘레 = 2(a + b) > minimum
# 넓이 = a * b > a,b는 N의 약수수

def solution(N):
    candidate = 0
    for i in range(1, int(N**(1/2)+1) + 1):
        if N % i == 0:
            perimeter = 2 * (i + N// i)
            if candidate == 0 or candidate > perimeter:
                candidate = perimeter
    return candidate

if __name__ == "__main__":
    N = 30

    print(solution(N))
