#program to print the fibonacci sequence

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
        