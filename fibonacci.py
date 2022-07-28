#program to print the fibonacci sequence
'''
nterms=int(input("enter the two values"))
n1,n2=0,1
count=0

if (nterms<=0):
    print('please enter the positive number')
elif(nterms==1):
    print('fibonacci sequence upto',nterms,':')
    print(n1)
else:
    print('fibonacci sequence:')
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=
     '''
     
#program to check if the number is  amstrong number or not  for( 3digits)
'''
num1=1
num2=1000

for x in range(num1,num2):
    y=len(str(x))
    sum=0
    temp=x
    while temp>0:
        digit=temp%10
        sum+=digit**y
        temp//=10
    if x==sum:
        print('it is an amstrong number',x)
'''
#program to find the sum of natural number
 
num1=1
num2=5

for x in range(num1,num2):
    while x>0:
        sum=0
        sum+=x
        x-=1
        print(sum)