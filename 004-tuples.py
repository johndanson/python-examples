# ############################################################################
# Tuples are composite data lists, that cannot be modified
# ############################################################################

markup_list = ["html", "css", "javascript", "chrome", 404]
print(markup_list)
markup_list[0] = "Jay Pedersen"
del markup_list[2]
print(markup_list)
print(markup_list[0], "uses", markup_list[2], "for Nike")



