import re
def solution(N):
    # Implement your solution here

    binary = bin(N)[2:]
    p = re.compile('1+')
    binary_rstrp = binary.rstrip('0')
    zero_list = p.split(binary_rstrp)

    return len(max(zero_list))