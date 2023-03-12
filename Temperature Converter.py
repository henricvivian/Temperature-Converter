def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Welcome to the temperature converter!")
while True:
    choice = input("Choose an option:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Quit\n")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        print(celsius, "degrees Celsius is equal to", celsius_to_fahrenheit(celsius), "degrees Fahrenheit.\n")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(fahrenheit, "degrees Fahrenheit is equal to", fahrenheit_to_celsius(fahrenheit), "degrees Celsius.\n")
    elif choice == "3":
        break
    else:
        print("Invalid input. Please try again.\n")

print("Thanks for using the temperature converter!")
