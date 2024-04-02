# score = 12 > 25
def solution(A, K):
    if not A:
        return A
    # Implement your solution here
    K = K % len(A)
    
    if K == 0:
        return A
    return A[-K:] + A[:-K]

if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    K = 3
    print(solution(A,K))