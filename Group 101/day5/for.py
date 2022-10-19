

a = "qwerty"
b = "asdfgh"


i = 0
while i < len(a):
    print(a[i] + b[i])
    i += 1    


menu = []


for i in range(5):
    food = input("type food: ")
    if "a" in food:
        menu.append(food)


print(menu)
