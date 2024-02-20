#bmi calculator 

print("Welcome to the bmi calculator")
heightX = float(input("What is your height in cms?"))
weightX = float(input("What is your weight in kgs?"))
heightInMetres = float(heightX) / 100
bmiResult = round(weightX / heightInMetres ** 2, 1)
print(f'your bmi is {bmiResult}')

if bmiResult >= 30:
    print("you are Obese.")
elif bmiResult >= 25:
    print("you are overweight.")
elif bmiResult >= 18.5:
    print("you are healthy")
else:
    print("you are underweight")
