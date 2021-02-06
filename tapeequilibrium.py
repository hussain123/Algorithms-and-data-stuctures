def solution(A):
    i = 1
    min = abs(sum(A[0:i+1])- sum(A[i+1:])) 
    while i < len(A)-1:
        
        difference =  abs(sum(A[0:i+1])- sum(A[i+1:])) 
        if difference< min:
            min = difference
        i +=1
def optimized(A):
    i = 1 
    array_left = []
    sum_left = 0
    j = len(A) -1
    sum_right = 0
    while j>0:
        sum_right += A[j]
        j -=1
        array_left.append(sum_right)
    
    sum_left = A[0]
    min = 100001
    while i < len(A):
        result = abs(sum_left - array_left[-i])
        
        if  result<min:
            min = result

        sum_left += A[i]
        
        i +=1
    return min 

if __name__ == "__main__":
    A = [3,1,2,4,3]
    print(optimized(A))