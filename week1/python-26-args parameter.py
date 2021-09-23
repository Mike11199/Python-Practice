# *args = parameter that will pack all arguments into a tuple
#           useful so that a function will accept a varying amount of arguments
#           asterisk * is most important - name can be anything, doesn't have to be args
#           does form of packing, taking all arguments and packing them into a tuple



def add(*args):
    sum = 0
    args = list(args)    #tuple is not mutable or changeable; need to convert it to a different collection by casting it to a list
    args[0] = 0
    for i in args:
        sum +=i           # the "+=" is the addition assignment operator.  shorhand for sum = i + i
    return sum


print(add(1,2,3,4,5,6))


