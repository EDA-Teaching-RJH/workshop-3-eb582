username = "Admin"
password = "Password123"
input_user = input("Input Username ")
input_pass = input("Input Password ")
if input_user == username and input_pass == password: print("Welcome Back Admin!")
if input_user != username and input_pass == password: print("Error Access Denied")
if input_user == username and input_pass != password: print("Incorrect Password")
if input_user != username and input_pass != password: print("Error Access Denied")