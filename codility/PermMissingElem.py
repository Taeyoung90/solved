def solution(A):
    
    max_num = len(A) + 1
    sum_to_max = int(max_num*(max_num+1) / 2)
    answer = sum_to_max - sum(A)
    
    return answer

if __name__ == "__main__":
    A = [2,3,1,5] # 7

    print(solution(A))