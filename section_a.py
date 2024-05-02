# a).(i)program to return student code
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    elif 50 <= percentage < 60:
        return 'E'
    else:
        return 'Fail'

def main(): # function for error handling and accepting user input
    
    try:
        percentage = float(input("Enter the percentage grade: "))
        if 0 <= percentage <= 100:
            grade = calculate_grade(percentage)
            print("The corresponding grade is:", grade)
        else:
            print("Percentage grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()


# (ii) convert to and from celcius to fahrenheit
def celsius_to_fahrenheit(celsius):
    #Convert temperature from Celsius to Fahrenheit.
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    #Convert temperature from Fahrenheit to Celsius.
    return (fahrenheit - 32) * 5/9

def main():
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Check if this script is being run directly
if __name__ == "__main__":
    main()




# b)(i)
def calculate_triangle_area(base, height):
    #Calculate the area of a triangle.
    return (1/2) * base * height

def main():
    # Input base and height from the user
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    # Calculate the area of the triangle
    area = calculate_triangle_area(base, height)

    # Print the result
    print("The area of the triangle with base", base, "and height", height, "is:", area)

if __name__ == "__main__":
    main()
    
    
    #(ii)python function to sum all numbers in a list
    
def sum_list_numbers(sample_list):
    #Sum all numbers in a list.
    total = 0
    for num in sample_list:
        total += num
    return total

# list
sample_list = [9, 2, 3, 5, 8]

# Calculate the sum of the numbers in the list
total_sum = sum_list_numbers(sample_list)

# Print the result
print("The sum of all the numbers in the list is:", total_sum)
