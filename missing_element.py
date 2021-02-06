def solution (A):
    pass

if __name__  == '__main__':
    A  = [2,3,1,5]
    sum = 0
    for i in range(1, len(A)+2):
        sum += i
    sum2 = 0
    for i in A:
        sum2 += i 
    print(sum - sum2)
    solution(A)