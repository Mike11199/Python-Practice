# while loop = a statement that will execute its block of code, as long as it's condition remains true

# while 1==1:
#     print("Help!  I'm stuck in a loop!")

name = None

while not name:
    name = input("Enter your name: ")

print("Hello "+name)