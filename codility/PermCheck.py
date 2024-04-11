# 100
def solution(A):
    set_a = set(A)
    if len(A) == len(set_a) and len(set_a) == max(A):
        return 1
    else:
        return 0

if __name__ == "__main__":
    A = [1,1] 

    print(solution(A))