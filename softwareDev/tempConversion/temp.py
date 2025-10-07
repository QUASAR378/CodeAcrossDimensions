#temp conversion program
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kelvin to Celsius")
    print("4. Celsius to Kelvin")
    print("5. Kelvin to Fahrenheit")
    print("6. Fahrenheit to Kelvin")
    choice = input("Choose a conversion (1-6): ")
    temp = float(input("Enter the temperature to convert: "))
    
    if choice == '1':
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    elif choice == '2':
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    elif choice == '3':
        result = kelvin_to_celsius(temp)
        print(f"{temp}K is {result}°C")
    elif choice == '4':
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C is {result}K")
    elif choice == '5':
        result = kelvin_to_fahrenheit(temp)
        print(f"{temp}K is {result}°F")
    elif choice == '6':
        result = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is {result}K")
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
