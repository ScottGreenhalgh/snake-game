name = raw_input("What is your name? ")
age = input("What is your age in years?")
height = input("How tall are you in meters?")
seconds = int(age)*60*60*24*365.25
feet = float(height)*3.28084
print("Hi %s, you are %s seconds old and %s feet tall!" % (name, seconds, feet)) 
