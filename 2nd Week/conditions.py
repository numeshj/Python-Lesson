x = 5
y = 20
z = 100

# Initialize a variable to store the maximum value
max_value = x

# Check if y is greater than the current max_value
if y > max_value:
    max_value = y

# Check if z is greater than the current max_value
if z > max_value:
    max_value = z

# Print the maximum value
print("The highest value is:", max_value)


# ---------------------- 2nd Method -------------------------
x = 5
y = 20
z = 100

# Finding the maximum value among x, y, and z
max_value = max(x, y, z)

# Printing the maximum value
print("The highest value is:",max_value)