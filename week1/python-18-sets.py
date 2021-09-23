# set = collection which is unordered, unindexed.  No duplicate values.  Faster than a list to check if something is in a set.  No duplicate values.

utensils = {"fork","spoon","knife", "knife","knife","knife"}
dishes = {"bowl","plate","cup","napkin","knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# dishes.update(utensils)

# for x in dishes:
#     print(x)

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(dishes.intersection(utensils))
