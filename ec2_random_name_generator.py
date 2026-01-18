# Moduel to generate random characters
import random
# Module to access letters and digits
import string

# Authorized Departments 
allowed_departments = ["marketing", "accounting", "finops"]

# Ask user how many EC2 name to generate
ec2_instances = int(input("How many EC2 instances do you want to name?\n"))

# Ask user what their department is
department_name = input("Enter your department): ")

# Convert department input to lowercase for easy comparison
department_name = department_name.lower()

# Verify if the department is authorized to use this generator
if department_name not in allowed_departments:
    # Print message if department is not approved
    print("This department is not authorized to use EC2 Name Generator.")
    # Stop the script so no names are generated
    exit()

for i in range(ec2_instances):
    # Generate 6 random uppercase letters
    random_letters = ''.join(random.choices(string.ascii_uppercase, k=6))
    # Generate 4 random digits
    random_digits = ''.join(random.choices(string.digits, k=4))
    # Build the final EC2 name using department + random characters
    ec2_name = department_name.capitalize() + "-" + random_letters + random_digits
    # Print the generated EC2 name
    print(ec2_name)
