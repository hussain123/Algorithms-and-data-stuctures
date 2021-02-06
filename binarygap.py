def optimized(bn, max_seq):
    if (len(bn) == 1):
        return max_seq
    
    first_one = bn.find('1')
    second_one = bn[first_one+1:].find('1')
    gap = (second_one - first_one) - 1
    if gap>max_seq:
        max_seq = gap

    return optimized(bn[second_one+1:], max_seq) 

def solution(N):

    # write your code in Python 3.6
    
    bn = '{0:b}'.format(N)
    print (optimized(bn,0))
    binary_length = len(bn)
    gap = 0
    max_seq = gap
    i = 0
    cycle = 0
    while  i < binary_length:
        j = i+1
        while bn[i] == '1' and  j < binary_length and bn[j] == '0':
            gap += 1
            j +=1
            cycle +=1
        
        if binary_length == j and bn[j-1] == '0':
            gap = 0
        else:
            if gap > max_seq:
                max_seq = gap
            gap = 0
        
        i = j
        
    print(cycle)
    return max_seq
if __name__ == "__main__":
    N = 505
    bin_num = '{0:b}'.format(N)
    print('{0:b}'.format(N))
    print(solution(N))


    