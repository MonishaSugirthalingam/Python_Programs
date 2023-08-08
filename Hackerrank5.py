def print_formatted(n):
    for i in range(1,n+1):
        print(i,end="  ")
        a=oct(i)
        print(a[2:],end="  ")
        b=hex(i)
        h=b[2:]
        if h.isalpha():
            print(h.upper(),end="  ")
        else:
            print(h,end="  ")
        c=bin(i)
        print(c[2:])
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
