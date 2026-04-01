number = int(input("enter no. of people:"))
rent1  = int(input("enter your Hotel rent:"))

rent2 = int(input("enter your Cab rent:"))
oil = int(input("enter your oil expenses:"))
food = int(input("enter your food expenses:"))
print("Everyone should pay:" )
output = (rent1 + rent2 + oil + food) // number
print(output)


