# Write a program to find whether a given number is prime or not.
n = int(input("Enter a number: "))

if(n==1):
    print("1 is neither prime nor composite")
    exit
elif(n<=0):
    print("You enter negitive or zero")
    exit
else:
    for i in range(2, int(n/2)):
        if(n%i) == 0:
            print("Number is not prime")
        break
    else:
        print("Number is prime")

