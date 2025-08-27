from math import*
def sum_digit(n):
    tong = 0 
    while n != 0:
        tong += n % 10
        n //= 10
    return tong
t = int (input())
for _ in range (t):
    n = int (input())
    a = list (map (int , input().split()))
    a.sort(key = lambda x :(sum_digit (x) , x))
    for x in a :
        print (x, end = ' ')
    print ()