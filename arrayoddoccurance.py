def solution(A):
    for i in range(0, len(A)):
        j = i+1
        even_counter = 1
        while j < len(A):
            if A[i] == A[j]:
                even_counter +=1
                A.pop(j)
            else:
                j +=1
            

        if even_counter % 2 == 1:
            return A[i]

def optimized(A):
    pairs= {}
    for i in A:
        if i not in pairs:
            pairs[i] = 1
        else:
            pairs[i]  = pairs[i] +1
    for i in pairs: 
        if  pairs[i] % 2 !=0:
            return i 
def getOddOccurrence(arr): 
  
    # Initialize result 
    res = 0
      
    # Traverse the array 
    for element in arr: 
        # XOR with the result 
        print(res ^ element) 
        res = res ^ element 
        print(res)
  
    return res 
if __name__ == "__main__":
    A =  [ 2, 3, 5, 4, 5, 2, 4] 
    print(getOddOccurrence(A))