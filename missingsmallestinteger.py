# missing smallest integer from an unsorted array 
#igore first solution 
# minimum value can be 1 for -ve numbers print 1 if missing 

def solution(A):
    
    if len(A) == 1:
        if A[0]<0:
            return 1
        return A[0] +1
    s = {}
    max_value = max(A)
    for i in range(1, max_value+2):
        s[i] = False
    for i in A:
        if i in s:
            s[i] = True

    for i in s:
        if not s[i]:
            return i
    return 1
def optimized(A):
    s = set()
    for i in A:
        if i>0:
            s.add(i)
    result = 1
    while result in s:
        result +=1

    return result
if __name__ =='__main__':
    A =  [1, 3, 6, 4, 1, 2]
    B = [1, 2, 3]
    C = [-1, -3]
    D =[-3,-1,0,1,2]
    F = [-5,-4,-3,-2,1,2,3,4,5,6,7]
    G = [0, 10, 2, -10, -20]
    H = [1,2,3,4,5,100,101,103,104,105]
    #print(optimized([-30]))
    print(optimized(H))
    print(solution(H))
    # print(solution(C))
    # print(solution(B))
    # print(solution(A))
    # print(solution([-1,0,2,4]))
    # print(solution([]))