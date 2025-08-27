s = input()
cnt4, cnt7 = 0, 0
for x in s :
    if x == '4':
        cnt4 += 1
    elif x == '7':
        cnt7 += 1
if cnt4 + cnt7 == 4 or cnt4 + cnt7 ==7 :
    print ("YES")
else :
    print ("NO")