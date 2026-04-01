from datetime  
import numpy
Dob = input("Enter your DOB: ")
x = datetime.strptime(Dob, "%d-%m-%Y").date()
today = date.today()
age = today.year - x.year - ((today.month, today.date)-(x.month, x.date))
print(age)