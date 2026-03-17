rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    
    # Descending
    for j in range(i, 0, -1):
        print(j, end="")
    
    # Ascending
    for j in range(2, i + 1):
        print(j, end="")
    
    print()
