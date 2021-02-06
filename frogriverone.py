def solution(A, X):

    i = 0
    d ={}
    
    print(s)
    while i<len(A):
        d[A[i]] = A[i]
        
        if len(d) == X:
            return i
        i +=1
    return -1
if __name__ == "__main__":
    A = [1,3,1,4,2,3,5,4]
    print(solution(A,4))