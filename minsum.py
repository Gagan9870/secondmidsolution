size=int(input())
lst=input().split()
c=list(map(int,lst))
b=[]
for i in range (size-1):
    a=c[i]-c[i+1]
    b.append(abs(a))
print(min(b))
