# Prompt the user to enter the number of rows
rows = int(input("Enter the number of rows: "))

# Print the pattern of asterisks in the form of a right triangle
for i in range(1, rows + 1):
    print('*' * i)
