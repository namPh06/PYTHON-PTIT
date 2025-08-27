s = input()
cnt1 , cnt2 = 0 ,0  
for x in s :
    if x.isupper():
        cnt1 += 1
    elif x.islower():
        cnt2 += 1
if cnt1 > cnt2 :
    s = s.upper()
    print (s)
else :
    s = s.lower()
    print (s)