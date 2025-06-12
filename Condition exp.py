#Ternary operator
#Formula X if condition else Y

num = 5
a = 5
b = 3
age = 27
temperature = 19
user_role = "admin"

#print("Positive" f num > 0 else "Negative")
#result = "EVEN" if num % 2 == 0 else "000"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather = "VERY HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)