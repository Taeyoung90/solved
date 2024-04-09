# 27 > 54(time limit)
import time

def solution(X, A):
    if len(set(A)) != X:
        return -1
    else:
        leave_position = [0]*X
        for time, position in enumerate(A):
            if leave_position[position-1] ==0:
                leave_position[position-1] = 1
                X -= 1
            if X == 0:
                return time     

    # leave_position = [0]*X
    # for time, position in enumerate(A):
        
    #     leave_position[position-1] = 1
    #     if sum(leave_position) == len(leave_position):
    #         return time    


if __name__ == "__main__":
    A = [1,3,1,4,2,3,5,4] # 6
    X = 5
    start = time.process_time()
    print(solution(X, A))
    print(time.process_time() - start)