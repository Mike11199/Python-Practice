# slicing = create a substring by extracting elements from another string
#   indexing [] or slice()
#   [start:stop:step]

name = "Jebediah Kerman"

first_name = name[:9]
last_name = name[9:]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)
print(website[slice])
print(website2[slice])