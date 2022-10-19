
weight = int(input("type your weight: "))
height = float(input("type your height: "))

bmi = weight / height**2



if bmi < 18.5:
        print("სუსტი წონა")
elif bmi >= 18.5 and bmi < 25:
    print ("ნორმალური წონა")
elif bmi >= 25 and bmi < 30:
    print("ცოტაოდენი წონის გადაჭარბება") 
elif bmi > 30:
    print("მსუქანი ხარ")
else:
    print("შედეგი უცნობია")               

        