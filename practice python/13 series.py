#1+2+3+--------+n
n=int(input("Input last number: "))
sum=0
for x in range(1,n+1,1):
    print(x)
    sum=sum+x
print("sum",sum)
#2+4+6+--------+n
n=int(input("Input last number"))
sum=0
for x in range(2,n+1,2):
    print(x)
    sum=sum+x
print("sum",sum)