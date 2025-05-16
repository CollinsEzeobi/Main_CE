#Get user travelling inputs
city_flight=input("Enter your destination(London,Tokyo,Madrid):")
num_nights=int(input("Number of nights you will be staying at a hotel:"))
rental_days=int(input("The number of days that you will be hiring a car:"))

def hotel_cost(num_nights):
   per_night= 500  
   return num_nights * per_night

#flight cost
def plane_cost(city_flight):
    if city_flight == "London":
        return 4500
    elif city_flight == "Tokyo":
        return 7000  
    elif city_flight == "Madrid":
        return 4000
    else:
         print("Invalid city. Choose between: London, Tokyo, Madrid")
         return 0 
    
def car_rental(rental_days):
    price_per_day = 500
    return rental_days * price_per_day

#Calculating cost of trip
def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel = hotel_cost(num_nights)      
    total_plane = plane_cost(city_flight)     
    total_rental = car_rental(rental_days)    
    total = total_hotel + total_plane + total_rental  
    return total 
total_cost = holiday_cost(num_nights, city_flight, rental_days)

print("\nHoliday destination:")
print(f"City: {city_flight}")
print(f"Number of nights in hotel: {num_nights}, Hotel cost: R{hotel_cost(num_nights)}")
print(f"Number of days renting car: {rental_days}, Car rental cost: R{car_rental(rental_days)}")
print(f"Flight cost: R{plane_cost(city_flight)}")
print(f"Total holiday cost: R{total_cost}")