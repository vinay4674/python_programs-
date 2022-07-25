#program to find the factorial of a number


n=int(input("enter the factorial number:" ))
factorial=1
if (n<0):
    print('sorry factorial not exist for negative number') 
elif(n==0):
    print('factorial of 0 is 1')
else:
    for i in range(1,n+1):
        factorial=factorial*i
        print('factorial of ',n,'is',factorial)