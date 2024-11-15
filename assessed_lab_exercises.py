def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operator == "-":
        result = num1 - num2


    # Function implementation here ...
        print(f"The result is: {result}")
    # Use elifs for every operator to apply calculations to the 2 numbers where neccesary.
    elif operator == "*":
        result = num1 * num2
        print(f"The result is: {result}")
    elif operator == "/":
        result = num1 / num2
        print(f"The result is: {result}")
    elif operator == "%":
        result = num1 % num2
        print(f"The result is: {result}")
    elif operator == ">":
        result = num1 > num2
        print(f"The result is: {result}")
    elif operator == ">=":
        result = num1 >= num2
        print(f"The result is: {result}")
    elif operator == "<":
        result = num1 < num2
        print(f"The result is: {result}")
    elif operator == "<=":
        result = num1 <= num2
        print(f"The result is: {result}")
    else:
        # Print invalid operator as every valid operator has been used before it
        print("Invalid operator.")

    return result

## Run the example
calculator(4, 5, "*")  # Output: The result is: 20
calculator(10, 2, "/")  # Output: The result is: 5.0
calculator(7, 7, ">=")  # Output: The comparison result is: True
calculator(10, 11, "<=")



def max_of_three(num1, num2, num3):
    # Check which numbers are more than or equal to the other numbers and make the highest the maximum
    if num1 >= num2 and num1 >= num3:
        maximum = num1
    elif num2 >= num1 and num2 >= num3:
        maximum = num2
    else:
        maximum = num3

    return maximum

# # You are out of the body function where you can test your code.
# Example usage:
maximum = max_of_three(10, 20, 30)
print(maximum, "is the maximum")



def are_anagrams(str1, str2):

    if len(str1) != len(str2):
        return False
    
    letter_count = {}
    
    # Count letters in the first string
    for i in str1:
        letter_count[i] = letter_count.get(i, 0) + 1
    
    # Decrease the count for letters in the second string
    for i in str2:
        if i in letter_count:
            letter_count[i] -= 1
            if letter_count[i] < 0:
                return False
        else:
            return False
    
    return True


## Example 
print(are_anagrams("listen", "silent"))  # Expected output: True
print(are_anagrams("hello", "world"))    # Expected output: False
print(are_anagrams("heart", "earth"))    # Expected output: True




def calculate_average(numbers):

    sum = 0
    # Loop through the numbers and add them all together
    for num in numbers:
        sum += num
    # Get the average by diving the sum of the numbers by the length of the list, as that tells you how many numbers there are.
    average = sum / len(numbers)

    return average

# # Example usage
numbers = [10, 20, 30, 40, 50]
print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0

numbers = [1, 4, 5, 6]
print("The average is:", calculate_average(numbers)) 




def calculate_weekly_pay(hours_worked):
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    # Function implementation here ...

    # Check if the hours worked is less than or equal to the standard hours and if so apply the regular rate
    if hours_worked <= standard_hours:
        total_pay = hours_worked * regular_rate
    else:
        # Calculate the overtime hours by getting the difference of the hours worked by the standard hours
        standard_pay = standard_hours * regular_rate
        overtime_hours = hours_worked - standard_hours
        # Calcualte the overtime pay by multiplying the overtime hours by the overtime rate and then get the total by adding the 2 pay totals together
        overtime_pay = overtime_hours * overtime_rate
        total_pay = standard_pay + overtime_pay
   
    return total_pay
    
# # Code Example
total_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
print(total_pay)



def is_prime(num):

    # Function implementation here ...


    # Check if the num is 1 or less than it and return false if so
    if num <= 1:
        return False
    # Loop through the number and calculate if its divisible by itself and 1 by seeing if it has a remainder
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

# # # Run code example
boolean = is_prime(5)   # returns True
print(boolean)


  

def sum_of_evens(min_value, max_value):
    # Create empty lists
    sum_nums = []
    values_range = []
    # Get the range of the minimum and maximum values
    values_range = range(min_value, max_value)
    # Loop through the range and check if the values are even and if so add them to the sum list
    for i in values_range:
        if i % 2 == 0:
            sum_nums.append(i)
        else:
            continue
    
    # Get the total by using the sum function on the list of numbers to be summed
    total = sum(sum_nums)
    return total

# # # Run code example
min_value = 10
max_value = 13
total = sum_of_evens(min_value, max_value) # returns 22
print(total)




def celsius_to_fahrenheit(celsius):

   output = celsius * (9/5) + 32
   return output
   

print(celsius_to_fahrenheit(20))




def decrypt_cypher_text(encrypted_text, key):

    # Get an empty string for the decrypted text
    decrypted_text = ""

    for letter in encrypted_text:
        # Convert the letters to ascii
        ascii_code = ord(letter)
        # Subtract the ascii code from the key and get the remainder of dividing it by 256
        new_code = (ascii_code - key) % 256
        # Get the decrypted letter by converting the new code to a character
        decrypted_letter = chr(new_code)
        # Add the decrypted letters to the decrypted text string
        decrypted_text += decrypted_letter

    return decrypted_text

print(decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$", 3))




def find_maximum_difference(a, b):
    # Get the minimum and maximum values of the lists a and b
    min_a = min(a)
    min_b = min(b)
    max_a = max(a)
    max_b = max(b)

    # Get 2 possible results of the difference between the maximums and minimums of a and b
    result_a = max(a) - min(b)
    result_b = max(b) - min(a)

    # Check which of the 2 results is greater, as that would therefore be the greater difference
    if result_a > result_b:
        maximum = result_a
    else: 
        maximum = result_b

    return maximum

print(find_maximum_difference([1,5 ,600], [100 ,7, 3 , 602, 39]))



def fuel_cost(distance_miles):
    # Constants
    MPG = 50  # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  # Price in pounds per liter

    total_cost = PRICE_PER_LITER * distance_miles / MPG * 4.5

    return total_cost

print(f"£{fuel_cost(50)}")




def is_golden_number(n):
    # Loop through all the numbers from 1 to n 
    for a in range(1, n):
        # Check if n is the sum of a and b by seeing if b is the difference between n and a
        b = n - a
        # Check if a * b is divisible by 1000 and if n is less than 1000 and return true if so
        if (a * b) % 1000 == 0 and n < 1000:
            return True
    return False


print(is_golden_number(13))



def km_to_miles(kilometers):
    #Calculate the miles by multiplying the kilometers by 0.62 and returning the result as a float
    miles = float(kilometers * 0.62)

    return miles

print(km_to_miles(120))




def letter_occurrence(input_string):
    #Set count to 0
    count = 0
    #Loop through each letter in the string
    for letter in input_string:
        #Check if its an a
        if letter == 'a' or letter == 'A':
            #increase the count by 1 if it is
            count += 1
    return count

print(letter_occurrence("Amazingly an ambitious one"))





def annual_net_income(gross_salary):
    #check if the gross salary is less or more than the tax brackets
    if gross_salary >= 45000:
        #calculate the net salary by taxing the gross salary
        net_salary = gross_salary * (1 - 0.5)
    elif gross_salary >= 30000:
        net_salary = gross_salary * (1 - 0.3)
    else:
        net_salary = gross_salary * (1 - 0.15)
    
    return net_salary

print(annual_net_income(20000))
        




