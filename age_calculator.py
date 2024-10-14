def calculate_age(current_date, current_month, current_year, 
                   birth_date, birth_month, birth_year):

    # Create a list of days in each month, considering February as 28 days (non-leap year)
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust the current date and month if the birth date is greater than the current date
    if birth_date > current_date:
        current_month -= 1
        current_date += months[birth_month - 1]
    
    # Adjust the current year and month if the birth month exceeds the current month
    if birth_month > current_month:
        current_year -= 1
        current_month += 12
    
    # Calculate the age in years, months, and days
    age_years = current_year - birth_year
    age_months = current_month - birth_month
    age_days = current_date - birth_date
    
    # Print the present age
    print("Present Age:")
    print(f"Years: {age_years}, Months: {age_months}, Days: {age_days}")


# Get input from the user
print("Enter the current date (dd/mm/yyyy):")x
current_date = int(input("Day: "))
current_month = int(input("Month: "))
current_year = int(input("Year: "))

print("Enter your birth date (dd/mm/yyyy):")
birth_date = int(input("Day: "))
birth_month = int(input("Month: "))
birth_year = int(input("Year: "))

# Calculate the age
calculate_age(current_date, current_month, current_year, 
              birth_date, birth_month, birth_year)
