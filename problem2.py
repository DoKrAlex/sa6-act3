# List of strings
strings = ["banana", "apple", "orange", "grape", "kiwi", "pear", "peach"]

# Sort the list based on length and then alphabetically
sorted_strings = sorted(strings, key=lambda x: (len(x), x))

# Print the sorted list
print("Sorted list of strings:", sorted_strings)
