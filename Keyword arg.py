#def hello(greeting, title, first, last):
   # print(f"{greeting} {title}{first} {last}")

#hello("Hello", title="Mr.", first="Spongebob",last="Squarepants")

#for x in range(1,11):
   # print(x, end=" ")

#print("1","2","3","4","5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="+91", area=8938, first=280, last=187)

print(phone_num)
