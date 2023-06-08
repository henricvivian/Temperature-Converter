def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def get_user_input(prompt):
    return input(prompt)

def print_conversion_result(from_unit, to_unit, converted_value):
    print(f"{from_unit} is equal to {converted_value} {to_unit}.\n")

def main():
    print("Welcome to the temperature converter!")
    while True:
        choice = get_user_input("Choose an option:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Quit\n")

        if choice == "1":
            celsius = float(get_user_input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print_conversion_result(celsius, "degrees Fahrenheit", fahrenheit)
        elif choice == "2":
            fahrenheit = float(get_user_input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print_conversion_result(fahrenheit, "degrees Celsius", celsius)
        elif choice == "3":
            break
        else:
            print("Invalid input. Please try again.\n")

    print("Thanks for using the temperature converter!")

if __name__ == "__main__":
    main()
