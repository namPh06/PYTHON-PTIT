def solve ( n , a ,b ,c):
    if n == 1 :
        print (f"{a} -> {c}")
    else :
        solve (n - 1, a, c,b)
        print (f"{a} -> {c}")
        solve (n- 1 , b,a ,c)
n = int (input())
solve (n , 'A' , 'B', 'C')
