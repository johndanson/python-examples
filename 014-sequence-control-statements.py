###############################################################################
# Sequence Control Statements (break and continue )
###############################################################################


# break
find_name = "Carter Smith"
for names in ["John Smith", "Keith Smith", "Sam Smith", "Job Smith", "Mark Smith"]:
    if names == find_name:
        print("break...", names, "has been found")
        break
else:
    print("break...", find_name, "was not found in the list")

print("\n")


# continue
find_name = "Sammy"
for names in ["John", "Kim", "Sammy", "Job", "Matt"]:
    if names == find_name:
        continue

print("continue...", names, "was found in list 3")

print("\n")

# sequence
find_name = "Dominique"
for names in ["John", "Sam", "Job", "May"]:
    print(names)
    if names == find_name:
        print(names, "has been found")
        break
if names != find_name:
    print("seq...", find_name, "was not found")



