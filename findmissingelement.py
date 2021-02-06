def solution(A):
    sum1 = 0
    for i in range(1, len(A)+2):
        sum1 += i
    sum2 = 0
    for i in A:
        sum2 += i
    return sum1-sum2
def optimized(A):
    pass

if __name__ == "__main__":
    A = [2,3,4,5,6,8]
    print(2^1)
    print(solution(A))


