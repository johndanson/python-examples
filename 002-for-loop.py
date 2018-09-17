# ############################################################################
# For loop with colon sections, if statements true and false.
# ############################################################################
find_name = "Dominique McGill"

print("\n")
for names in ["Johnny B. Good", "Kimmy Schmidt", "Sammy Davis Jr.", "Dominique McGill", "Matt LeBlanc"]:
    if names == find_name:
        continue

    print(names, "was found in the list")

print("\n")

for names in ["Johnny B. Good", "Kimmy Schmidt", "Sammy Davis Jr.", "Dominique McGill", "Matt LeBlanc"]:
    if names != find_name:
        continue

    print(names, " !!  was also found in the list")


