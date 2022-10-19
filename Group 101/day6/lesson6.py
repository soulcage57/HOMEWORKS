#ინფუთით შემოვიტანოთ სახელი და გვარი და ტერმინალში გამოვიტანოთ რომელ ინდექსზე არის ხმოვნები
# და ასევე გვაჩვენოს თუ შედის ამ სახელში "b" ასო ან "g" თუ შედის გვითხრას რომ შედის
#თუ სახელი არის ლუწი სიმბოლოების მაშინ გამოოიტანე სახელი ისე რომ პირველი ასო იყო დიდი 

name = str(input("type you name: "))


i = 0

while i < len(name):
    if name[i] in "aeiou":
        print(str(i)+ name[i])
    i += 1    



# x =0
# for i in range(5):
#     for j in range(4):
#         print(str(x) + "beka")
#         x +=1    

#დაიპრინტება თიქეთების სისტემა როცა ბილეთი ღირს 100$
total_price = 0
for i in range(5):
    age_of_user = int(input("enter users age: "))
    if age_of_user >= 3:
        total_price += 100



print(total_price)