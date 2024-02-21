MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        fahrenheit = float(input("Fahrenheit: "))
        celsius = (fahrenheit-32)*5/9
        print(f"result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")