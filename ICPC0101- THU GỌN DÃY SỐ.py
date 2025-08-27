n = int (input())
a = list (map (int , input().split()))
st = []
for x in a :
    if st and (x + st[-1]) % 2 == 0 :
        st.pop()
    else :
        st.append(x)
print (len (st))