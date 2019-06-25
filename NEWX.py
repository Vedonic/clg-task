def coat(val):
    global a,b,i
    s=''
    while(i<lmt-1):
        s+=a[i]
        s+=b[i]
        i+=1
    if val==1:
        s+=a[lmt:]
    elif val==2:
        s+=b[lmt:]
    print(s)

a=input('enter a string '.title())
b=input('enter another string '.title())
la,lb=len(a),len(b)
lmt,i=max(la,lb),0
if la>lb:
    coat(1)
elif la<lb:
    coat(2)
else:
    coat(0)
