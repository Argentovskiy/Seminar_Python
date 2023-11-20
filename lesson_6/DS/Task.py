
a1 = 2
d = 3
n = 4
count=1


def reknumb(a1,d,n,count):
    print(a1+(count-1)*d)
    count+=1
    if count-1==n:
        return 
    reknumb(a1,d,n,count)
    
reknumb(a1,d,n,count)