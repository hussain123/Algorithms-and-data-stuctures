def solution(A, N):
    # write your code in Python 3.6
    counters = [0] * (N)
    X = 0
    
    for K in A:
        if 1<= K <= N:
            if counters[K-1] ==X:
                X +=1
                counters[K-1] = X
            else:
                counters[K-1] = X
        else:
            counters = [X] * N 
    return counters
if __name__ == "__main__":
    A = [3, 4,4,6,1, 4, 4,8 ]
    B = [2, 1, 1, 2, 1]
    C = [2, -1, 3, 3, 4, 5]
    print(solution(A,5))


def optimized(A,N):
    counters = [0] * (N)
    X = 0
    
    for K in A:
        if 1<= K <= N:
            counters[K-1] += 1
            if counters[K-1] > X:
                X = counters[K-1]
        else:
             counters = [X] * N       
    return counters