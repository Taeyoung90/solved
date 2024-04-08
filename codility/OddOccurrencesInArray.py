# 66 > 66
from collections import Counter

def solution(A):
    count_dict = Counter(A)
    # 1번
    # for key , value in count_dict.items():
    #     if value == 1:
    #         return key
    # 2번
    return min(count_dict.keys(), key=(lambda k: count_dict[k]))

if __name__ == "__main__":
    A = [9,3,9,3,9,7,9] # 7
    print(Counter(A))
    print(solution(A))