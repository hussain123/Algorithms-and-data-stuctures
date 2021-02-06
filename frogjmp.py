def solution(X,Y,Z):
    pass

if __name__ == '__main__':
    X,Y,Z  = 10,86,5

    jumps = (Y-X)/Z
    print(type(jumps))
    if type(jumps) is float:
        print(int(jumps +1))
    print(jumps)

    if jumps > int(jumps):
        print(jumps+1)