# Section 1: Variables and Types

name = "Aktan"
age = 22
height = 6.02
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# Section 2: User Input and Math

user_name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

approximate_age = 2026 - birth_year

print(f"Hi, {user_name}! You are approximately {approximate_age} years old.")


# Section 3: Type Conversion and f-strings

number_one = float(input("Enter the first number: "))
number_two = float(input("Enter the second number: "))

product = number_one * number_two

print(f"{number_one} × {number_two} = {product}")


# Section 4: Formatted Receipt

item_name = "Pepperoni Pizza Pie"
price = 19.99
quantity = 2

total = price * quantity

print("===========================")
print("         RECEIPT")
print("===========================")
print(f"Item:      {item_name}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")


# Section 5: Mini-Project - Profile Card

profile_name = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("Tell me one fun fact about yourself: ")
profile_birth_year = int(input("What year were you born? "))

profile_age = 2026 - profile_birth_year

print()
print("╔══════════════════════════════╗")
print(f"      PROFILE: {profile_name}")
print("╚══════════════════════════════╝")
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun fact:   {fun_fact}")
print(f"Age:        {profile_age}")
