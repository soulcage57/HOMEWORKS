    #  მომხმარებელმა შემოიტანოს სამი რიცხვი 
    #  ამთგან კენტები შეკრიბოს და გამოიტანოს ჯამი



num1 = int(input("type number first: "))
num2 = int(input("type number two: "))
num3 = int(input("type number three: "))




def odd_sum(num1, num2 , num3):
    sum = 0
    if num1 % 2 ==1: 
        sum += num1

    if num2 % 2 ==1:
       sum += num2
    if num3 % 2 ==1:
       sum += num3
       print(sum)

odd_sum(num1, num2 , num3)

