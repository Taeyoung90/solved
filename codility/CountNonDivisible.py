# 55 > 66 >
'''
return : 각 원소의 약수가 아닌 원소의 개수 list

중복 원소 고려 : 각 원소별 개수가 몇개인지 사전으로 저장해두고
체크할때는 중복을 제거
> 66

내림차순 정렬 > 해당 숫자의 시작 위치를 부터 시작(더 큰 숫자는 무조건 약수가 아니므로)

한 번 계산한 원소의 값은 따로 저장해둠
> 조금 빨라졌으나 그래도 66

중복없는 리스트를 내림차순으로 놓고 각 원소에 대한 개수를 구해놓고 전체 문제리스트에 대한 결과값을 산출 > 동일하게 66

약수를 구할 시에 빠르게 할 수 있는 방법 사용 > 1부터 주어진 숫자의 root값까지만 확인해보면서 나누어 떨어질경우 짝약수도 바로 확인


'''
from time import time
from collections import Counter
import math

def calculatedivisor(num): # 약수 구하기
    divisors = []
    for i in range(1, math.trunc(math.sqrt(num))+1):
        if num % i ==0:
            divisors.append(i)
            if i ** 2 != num:
                divisors.append(num//i)
    
    return sorted(divisors)

def solution(A):
    count_A = Counter(A)
    answer = []
    result_dict = {}
    set_A = sorted(list(set(A)), reverse=True)
    print(calculatedivisor(100))
    # for ele in A:
    #     if  ele in result_dict.keys():
    #         answer.append(result_dict[ele])
    #         continue
    #     cnt = len(A)
    #     start_index = set_A.index(ele)
    #     for denominator in set_A[start_index:]:
    #         if ele % denominator == 0:
    #             cnt -= count_A[denominator]
    #     answer.append(cnt)
    #     if ele not in result_dict.keys():
    #         result_dict[ele] = cnt
            
    # for i, numerator in enumerate(set_A):
    #     cnt = len(A)
    #     for denominator in set_A[i:]:
    #         if numerator % denominator == 0:
    #             cnt -= count_A[denominator]
    #     result_dict[numerator] = cnt
    
    # answer = [result_dict[x] for x in A]
    
    for numerator in set_A:

        sqrt_num = math.trunc(math.sqrt(numerator))
        cnt = len(A)
        for denominator in range(sqrt_num+1):
            if denominator in set_A and numerator % denominator == 0:
                cnt -= count_A[denominator]
                divisor2 = numerator // denominator
                if divisor2 in set_A and divisor2 != denominator: # 약수의 제곱이 해당 수인 경우 제외
                    cnt -= count_A[divisor2]
        result_dict[numerator] = cnt
        
        if 1 not in set_A:
            result_dict[numerator] = cnt - count_A[numerator]
        
    answer = [result_dict[x] for x in A]        
                
    return answer

if __name__ == "__main__":
    # A = [3,1,2,3,6]w # 7
    A = [2,4]
    
    # A = [3,2]
    # A = [3,2,3,6]
    start_time = time()
    print(solution(A))
    print(time() - start_time)