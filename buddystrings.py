def Solution(A,B):
    original_string = A
    A = list(A)
    B = list(B)
    if len(A) !=len(B):
        return False
    seen = []
    if A == B:
        for i in A:
            if i in seen:
                return True
            else:
                seen.append(i)
        return False
    i =0 
    while i < len(A):
        if A[i] not in B or B[i] not in A :
            return False
        if A[i] != B[i]:
            j = i+1
            while A[i] != A[j]:
                if A[i] != A[j]:
                    temp  = A[i]
                    A[i] = A[j]
                    A[j] = temp
                    if A == B:
                        return True
                    else:
                        A = list(original_string)
                j +=1
        i +=1
if __name__ == '__main__':
    A="abcd"
    B = "cbad" # acbd
    #print(Solution(A,B))
    assert Solution('', 'aa') == False
    assert Solution('abbcdefghu', 'abcdd') == False
    assert Solution('aaaaaaabcd', 'aaaaaaabdc') == True
    assert Solution('abcdfefgaaaah', 'abcdfefhaaaag') == True
    assert Solution('aa', 'aa') == True
    assert Solution('', 'aa') == False
