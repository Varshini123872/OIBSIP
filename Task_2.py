try:
    weight=float(input("Enter your weight in (kg) : "))
    if weight<=0:
        raise ValueError("weight must be positive ")
    
    height=float(input("Enter your height in (m) : "))
    if height<=0:
            raise ValueError("height must be greater than 0")
    BMI=weight/(height**2)
    if (BMI<18.5):
        print(f"{BMI:.2f}Underweight")
    elif(BMI<24.9):
        print(f"{BMI:.2f}Normal")
    elif(BMI<29.0):
        print(f"{BMI:.2f}Overweight")
    else:
        print(f"{BMI:.2f}Obese")
except ValueError as e:
    print(e)


