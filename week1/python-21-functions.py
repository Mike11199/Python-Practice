# function = a block of code that is execute only when it is called

def hello (first_name,last_name,age):
    print("hello " +first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("have a nice day!")

myname = "Neo"

# hello("Jeb")         #sending an argument to a function with a matching number of parameters
# hello("person")
# hello(myname)

hello("Jeb","Kerman","21")