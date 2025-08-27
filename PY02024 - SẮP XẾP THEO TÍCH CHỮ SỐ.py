from math import*
def tich_digit(n):
    tich = 1 
    while n != 0:
        tich *= n % 10
        n //= 10
    return tich
t = int (input())
for _ in range (t):
    n = int (input())
    a = list (map (int , input().split()))
    a.sort(key = lambda x :(tich_digit (x) , x))
    for x in a :
        print (x, end = ' ')
    print ()