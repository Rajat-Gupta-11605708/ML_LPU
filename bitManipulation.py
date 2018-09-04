a=int(input())
b=int(input())
x=[]
y=[]
count1=0
count2=0
while(a>0):
    rem=a%2
    x.append(rem)
    a=a//2
    count1+=1
while(b>0):
    rem=b%2
    y.append(rem)
    b=b//2
    count2+=1

if(count1!=36):
    for i in range (36-count1):
        x.append(0)
if(count2!=36):
    for i in range (36-count2):
        y.append(0)

count3=0
for i in range (36):
    if(x[i]!=y[i]):
        count3+=1

x.reverse()
y.reverse()

print(count3)


