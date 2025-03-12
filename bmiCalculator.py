def heightToInches(height_feet, height_inches):
    if height_feet < 0 or height_inches < 0:
        raise ValueError
    height = (height_feet * 12) + height_inches
    return height

def inchesToMeters(inches):
    if inches < 0:
        raise ValueError
    meters = inches * 0.025 
    return round(meters, 2)

def poundsToKilos(pounds):
    if pounds < 0:
        raise ValueError
    kilos = pounds * 0.45
    return round(kilos, 2)

def calculateBMI(meters, kilos):
    if kilos < 0 or meters < 0:
        raise ValueError
    bmi = kilos / (meters ** 2)
    
    return round(bmi, 1)

def calculateCategory(bmi):
    if bmi < 18.5:
        category = "Underweight"
    elif bmi >=18.5 and bmi < 25:
        category = "Normal weight"
    elif bmi >=25 and bmi < 30:
        category = "Overweight"
    elif bmi >= 30:
        category = "Obese"
        
    return category
    

def main():
    while True:
        print("\nWelcome to the BMI Calculator.\n1.Calculate BMI.\n2.Convert pounds to kilos.\n3.Convert inches to meters.\n4.Convert height to inches.\n5.Exit.\n")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                height_feet = int(input("Enter your height (feet): "))
                height_inches = int(input("Enter your height (inches): "))
                weight = float(input("Enter your weight (pounds): "))
                bmi = calculateBMI(inchesToMeters(heightToInches(height_feet, height_inches)),poundsToKilos(weight))
                category = calculateCategory(bmi)
                print(f"BMI: {bmi}\nCategory: {category}\n")
            except ValueError:
                print("Invalid input, enter numeric values greater than 0.")
            except Exception:
                print(f"An error occured: {Exception}")
        elif choice == "2":
            try:
                pounds = float(input("Enter your weight (pounds): "))
                kilos = poundsToKilos(pounds)
                print(f"{pounds}lbs converts to {kilos}kgs.")
            except ValueError:
                print("Invalid input, enter numeric values greater than 0.")
            except Exception:
                print(f"An error occured: {Exception}")
        elif choice == "3":
            print("inches to meters")
        elif choice == "4":
            print("height to inches")
        elif choice == "5":
            break
        else:
            print("Invalid choice please try again.")
        

if __name__ == "__main__":
    main()