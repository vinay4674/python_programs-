# This program used to find prime numbers  

num=int(input("Enter the number to check prime or not:" ))

if(num>1):
	
	for n in range(2,num):
		if (num%n)==0:
		   print("it is not a prime number")
		   break
	
	else:
		print("it is a prime number")



else:

	print("it is not a prime number")
