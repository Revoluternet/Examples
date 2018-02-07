"""This program identify prime number that user Enter between his/her own range"""

import time
minimum = int(input("Enter Lower number: "))
maximum = int(input("Enter Upper Number: "))

#minimum =1
#maximum= 50

print("You Enter Lower number: ",minimum, "\n you Enter upper Number :",maximum)

print("prime numbers are: ")
if minimum == 1:
    print("\t\t 1")


for number in range(minimum,maximum+1):
    if number > 1:
        #prime number is greater than 1
        for i in range(2,number):

            if (number%i) == 0:
                break
        else:
           # print(end="[")
            print("\t\t",number)
            time.sleep(1)
