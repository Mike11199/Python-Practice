# keyword arguments = arguments preceded by an identifier when we pass them to a function.  The order of the arguments
#                     doesn't matter, unlike positional arguments.  Python knows the names of the arguments that
#                     our function receives.


def hello(first,middle,last):
    print("Hello "+first+" "+middle+" " + last)

hello("Michael","Smith","Johnson")   #order does matter - positional arguments

hello(last="Michael",middle="Smith",first="Johnson")   #order does matter - positional arguments
