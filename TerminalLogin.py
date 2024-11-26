# Step 1: Basic Python program to check if the password entered is correct or not
x=3
password="Password"

# Step 2: Add a loop to allow the user to enter the password again if the password is incorrect, and limit the number of attempts to 3,  and if the user fails to enter the correct password in 3 attempts, the program should terminate and display a message "You have exceeded the number of attempts, please try again later"
while x>0:
    passwordcheck=input("Please enter your password : ")
    if password == passwordcheck:
        print("Welcome back")
        break
    else:
        print("The credentials provided is incorrect")
        x=x-1
        if x==0:
            print("The password did not match this email address we hold on record")
            break

# Code without 3 attempt limitation
""" if password == passwordcheck:
    print("Welcome back")

else:
    print("The password did not match this email address we hold on record") """


# Future Work: Transfer login to stack
# Security Steps: Review the code to ensure that the password is not hardcoded in the code
# Security Steps: Check network traffic to see if the password entered is transmitted in plain text

# Future Work: Add a registration feature to allow the user to register and create a password
# Future Work: Add a feature to enable the user to reset the password if the user has forgotten the password
