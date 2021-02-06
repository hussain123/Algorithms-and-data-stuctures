import sys as sys
def solution(A, N):
    _min, second_min =sys.maxsize, sys.maxsize
    for i in A:
        if i< _min:
            second_min = _min
            _min = i
        elif i< second_min:
            second_min = i
    return second_min
def kth_smallest(arr,k):
    print(sorted(arr))
if __name__ == "__main__":
    A = [3, 4,4,6,1, 2, 4,8 ]
    print(sorted(A))
    #print(solution(A,2))
    
