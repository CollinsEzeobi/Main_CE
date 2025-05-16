num_students = int(input("How many students are registering? "))

file=open("reg_form.txt", "w")

for i in range(1, num_students + 1):
    ID = int(input(f"Enter Student ID for Student {i}: "))
   
    file.write(f"Student ID: {ID}\n{'-'*10}\n")
        
print(f"We will now commence the exam, Good Luck.")

file.close