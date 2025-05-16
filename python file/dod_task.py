# Open the file
with open("DOB.txt", "r") as file:
    names = []
    birthdates = []
    
    # Loop through each line
    for line in file:
        words = line.split()
        name = " ".join(words[0:2])  
        birthdate = " ".join(words[2:])  
        names.append(name)
        birthdates.append(birthdate)
        print("Name")
        
    for name in names:
        print(name)
        print() 
        print("Birthdate")
        
    for birthdate in birthdates:
        print(birthdate)

