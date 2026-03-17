rows = 5

# Upper
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)

# Lower
for i in range(2, rows + 1):
    print(" " * (rows - i) + "* " * i)
