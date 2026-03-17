rows = 5

# Top arrow
for i in range(1, rows+1):
    print(" " * (rows - i) + "* " * i)

# Shaft
for i in range(rows-1):
    print(" " * (rows - 1) + "*")
