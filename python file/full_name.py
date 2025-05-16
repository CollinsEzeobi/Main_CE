
#ask the user to input their full name
#if statement,else statement
#Operators
#"<"symbol for greater than
name= str(input("Enter your name?"))

if len(name) < 4:
  print("you have entered less than 4 chracters,please make sure that you enter your full name and surname.")
if len (name) > 25:
  print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
elif len(name) ==0:
  print("no input was detected ")
  
else:
  print("thank you for entering your name")
