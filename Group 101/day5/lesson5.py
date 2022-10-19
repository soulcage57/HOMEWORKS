# მომხმარებელმა შემოიტანოს ორი სახელი რომელშიც
# უფრო მეტი თანხმოვანი იქნება ის დაიპრინტოს

name1 = str(input("type name1: "))
name2 = str(input("type name2: "))

name1Consonant = 0
name2Consonant = 0

for char in name1:
    if char not in "aeiou":
        name1Consonant += 1

for char in name2:
    if char not in "aeiou":
        name2Consonant += 1        

if name1Consonant > name2Consonant:
    print(name1)
    print("pirveli saxelis tanxmovnebi metia meore saxelze da sheicavs {} tanxmovans".format(name1Consonant))
elif name1Consonant < name2Consonant:
    print(name2)
    print("meore saxelis tanxmovnebi metia pirvel saxelze da sheicavs {} tanxmovans".format(name2Consonant))
else:
    print("orive saxelis tanxmovnebi aris toli da sheicavs {} tanxmovans".format(name1Consonant))