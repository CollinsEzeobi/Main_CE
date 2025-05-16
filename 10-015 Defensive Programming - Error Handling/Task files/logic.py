#Ask the uer to enter three different integer
num1=int(input("enter the first integer:"))
num2=int(input("enter the second integer:"))
num3=int(input("enter the third integer:"))

#print out the sum of all the numbers
numbers_list=[num1,num2,num3]
print(f"sum of all the numbers:{sum(numbers_list)}")

#print the first number minus the second number
#(its "+" not "-")
print(f" the first number minus the second number:{num1+num2}")

#print out the third number multiplied by the first number
print(f"the third number multiplied by the first number:{num3*num1}")

#print out the sum of all 2 numbers divided by the number
#(logical error is that its 3 numbers)
print(sum(numbers_list) / 3)

