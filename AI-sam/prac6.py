# Fuzzy Set Operations

# Define two fuzzy sets
A = {"a": 0.5, "b": 0.6, "c": 0.7, "d": 0.8}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}

print("The First Fuzzy Set is:", A)
print("The Second Fuzzy Set is:", B)

# Union of two fuzzy sets
union = {}
for key in A:
    union[key] = max(A[key], B[key])
print("Fuzzy Set Union is:", union)

# Intersection of two fuzzy sets
intersection = {}
for key in A:
    intersection[key] = min(A[key], B[key])
print("Fuzzy Set Intersection is:", intersection)

# Complement of fuzzy set A
complement_A = {}
for key in A:
    complement_A[key] = 1 - A[key]
print("Fuzzy Set A Complement is:", complement_A)

# Difference (A - B)
difference = {}
for key in A:
    difference[key] = min(A[key], 1 - B[key])
print("Fuzzy Set Difference (A - B) is:", difference)
