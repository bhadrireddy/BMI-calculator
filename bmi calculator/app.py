name=input("Enter your name:")

weight=int(input("Enter your body weight in KG:"))

height=int(input("Enter your height in cm:"))
height_m = height / 100 
BMI=weight/(height_m**2)

print(BMI)
if BMI>0:
    if (BMI<18.5):
        print(name +", You are underweight.")
    elif(BMI<=24.9):
        print(name +", You are normal weight.")
    elif(BMI<18.5):
        print(name +", You are underweight.")
    elif(BMI<29.9):
        print(name +", You are overweight.")
    elif(BMI<34.9):
        print(name +",You are obese.")
    elif(BMI<39.9):
        print(name +",You are severely obese.")
    else:
        print(name+", you are morbidly obese.")
else:
    print("Enter a valid input")