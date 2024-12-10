# MVP 1: Pyton login page
"""
*** SECURITY CHECK ***
Login screen should not through any way increase the risk of Username Enumeration.

Do not provide any information that can be used to determine if a username is valid or invalid. This includes but is not limited to:
- Error messages that indicate whether a username is valid or invalid
- Different responses for valid and invalid usernames
- Different response times for valid and invalid usernames
- Different responses for valid and invalid usernames

**Action 1**
Open application
enter correct username
enter incorrect password
**Expected Result**
if incorrect password is entered notify user that the combination entered is not correct

**Action 2**
Open application
enter incorrect username
enter correct password
**Expected Result**
if incorrect username is entered notify user that the combination entered is not correct
"""

x=3
y=3
username="username"
password="password"

otp="1234"

while x>0:
    usernamecheck=input("Please enter your Username : ")
    passwordcheck=input("Please enter your Password: ")
    if username==usernamecheck and password == passwordcheck:
        x=0
        while y>0:
            otpcheck=input("Please enter OTP: ")
            if otpcheck == otp:
                print("Welcome back")
                break
            else:
                print("That is not right. Try Again")
                y=y-1
                if y==0:
                    print("You have exceeded the number of attempts, please try again later")
                    break     
    
    else:
        print("The credentials provided is incorrect")
        x=x-1
        if x==0:
            # ** Security Check **
            #AI Generated print("The password did not match this email address we hold on record") 
            #changed to:
            print("Are you sure you have the details right, the credential provided does not match. Try and reset your password") 
            # "or contact support" -- Do not have support as a actor identified in my use case but have future improvement identified as user experience.
            #BACKLOG: BLOG3 User experience: In case the user thinks they are providing the correct information or feels like they are going in a loop direct the user to other ways to authenticate or a page."""
            break
            
