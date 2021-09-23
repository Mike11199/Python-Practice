# scope = The region that a variable is recognized
#         A variable is only available from the region it is created.
#         A global and locally scoped versions of a variable can be created



#Python uses the LEGB rule
#  L = Local Variables first
#  E = Enclosing
#  G = Global
#  B = Built-in




name = "Neo" #global scope (available inside & outside functions)

def display_name():
    name = "Code"
    print(name)    #local scope (available only inside this function)

display_name()
print(name)




