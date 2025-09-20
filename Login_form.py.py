USERNAME = "kuljinder sharma"
PASSWORD = "Ram@123"


print ("===login page===")

username = input ("Enter userusername :")
password = input (" Enter passwrod :")

if username == USERNAME and password == PASSWORD:
    print ("welecome !", USERNAME)
else:
    print (" Not able to login, Incorrect password!",)    
