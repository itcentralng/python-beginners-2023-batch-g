# Q1. Write a website simulator that allows users to signup and signin.
#     Conditions for signup:
#           - Name
#           - Email(unique)
#           - Phone(unique)
#           - Password(atleast 5 characters)
#     Conditions for signin:
#           - Must have signed up already
#           - Email must be correct - case insensitive
#           - Password must be correct
# NOTE: At each stage notify the user witht the proper message



print("   SIGN UP HERE   ")

user_database={"name":"","Email":"","Password":"","Phone":""}
name=input("Type your name here :")
Email=input("Type your email here :")
Phone=input("Type your phone number here :")
Password=input("Type your password here(8 characters) :") 

if ("@" not in Email) and ("." not in Email):
    print("Invalid Email address" )
    if Phone.startwith("0") and len(Phone) == 11 and Phone.isidigit():
     if Password and len(Password)>=8:
        print("THANK YO FOR SIGNING WITH US")


