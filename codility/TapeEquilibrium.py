# 46
def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])
    
    min_difference = A[0] - sum(A[1:])
    diff_list = [min_difference]
    for a in A[1:-1]:
        diff_list.append(diff_list[-1]+2*a)
    
    answer = min(list(map(abs,diff_list)))
    
    return answer

if __name__ == "__main__":
    A = [3,1,2,4,3] # 6

    print(solution(A))