    #  მომხმარებელმა შემოიტანოს სამი რიცხვი 
    #  ამთგან კენტები შეკრიბოს და გამოიტანოს ჯამი



num1 = int(input("type number first: "))
num2 = int(input("type number two: "))
num3 = int(input("type number three: "))




sum = 0
if num1 % 2 ==0: 
    sum += num1

if num2 % 2 ==0:
    sum += num2
if num3 % 2 ==0:
    sum += num3

print(sum)  

