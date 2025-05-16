triathlon=input("Enter your traithlon time completed for:...first press enter...")
num1=float(input("swimming time:"))
num2=float(input("cycling time:"))
num3=float(input("running time:"))
time_total =(num1+num2+num3)
print("total time take:")
print(time_total) 

#the qualifying time for the award is 100  minutes
#time differents is = to the total time minus 100
qualifying_time=100 #qualifying time
time_difference= time_total- 100
# "<=" greater than or equal to symbol
# ">=" less than or equal to symbol
if time_total <= qualifying_time:
    print("provincial Colours")
elif time_difference <= 5:
    print("Provincial half colours")
elif time_difference <= 10:
    print("Provincial Scroll")
else:
    print("no award")

