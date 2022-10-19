# მომხმარებელმა შემოიტანოს ორი სახელი და 
# დაიპრინტოს ის სახელი რომელშიც უფრო მეტი ხმოვანი იქნება




name1 = input("type name1: ")
name2 = input("type name2: ")

name1sum = 0
name2sum = 0

for char in name1:
   if char in "aeiou":
      name1sum += 1

for char in name2:
   if char in "aeiou":
      name2sum += 1

if name1sum > name2sum:
   print(name1)

if name2sum > name1sum:
   print(name2)
   
if name1sum == name2sum:
   print("orive saxeli sheicavs {} xmovans da aris toli" .format(name1sum))