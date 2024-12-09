# MVP 1: Pyton login page
'''**Test Plan A**
**Action 1**
Run Program
User skips entering username
Expected Result
Error message: Username is required
**Action 2**
Run Program
User enters username but skips password
Expected Result
Error message: password is required
**Action 3**
Run Program
User enters username and password but skips OTP
Expected Result
Error message: OTP is required
**Action 4**
Run Program
User enters username, password and OTP
print welcome back'''

usernamecheck=""
passwordcheck=""
otpcheck=""
usernamecheck=input("Please enter username: ")

while usernamecheck == "":
    print("Username is required")
    usernamecheck=input("Please enter username: ")
    
passwordcheck=input("Please enter your password: ")
while passwordcheck=="":    
        print("Password is required")
        passwordcheck=input("Please enter your password: ")

otpcheck=input("Please enter OTP: ")
while otpcheck=="":
    print("OTP is required")
    otpcheck=input("Please enter OTP: ")

print("Welcome back")
