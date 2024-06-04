name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2024  # You can update this to the current year

age = current_year - year_of_birth
print("Hello", name, "! You are", age, "years old.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")