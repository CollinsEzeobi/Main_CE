# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
print ("Welcome to the error program\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" 
age = int(age_Str) 
print("I'm " + str(age) + " years old.")

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now)

print ("The total number of years: " + str( total_years ))

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old")


