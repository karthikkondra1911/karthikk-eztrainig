n=int(input("enter the numbers"))
i=0
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
print(sum)
#sum of digits
