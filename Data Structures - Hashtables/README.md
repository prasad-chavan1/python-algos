# Hash Tables in Python

Hash tables, also known as hash maps, are a fundamental data structure in computer science. They allow for efficient storage and retrieval of key-value pairs. In Python, hash tables are implemented using dictionaries. This README will explore the concept of hash tables and provide examples of their usage.

## Table of Contents

1. [First Recurring Character](#first-recurring-character)
2. [Hash Table Implementation](#hash-table-implementation)

## First Recurring Character

The problem of finding the first recurring character in a string can be efficiently solved using a hash table. Here's a brief explanation of how it works:

- Create an empty hash table (dictionary) to store characters as keys and their positions as values.
- Iterate through each character in the string.
- For each character, check if it's already in the hash table.
  - If it's not in the hash table, add it with its position.
  - If it's already in the hash table, you've found the first recurring character.

Here's a Python code snippet to find the first recurring character:

```python
def find_first_recurring_character(string):
    char_position = {}
    for index, char in enumerate(string):
        if char in char_position:
            return char
        char_position[char] = index
    return None

# Example usage:
input_string = "abcdefa"
result = find_first_recurring_character(input_string)
print("First recurring character:", result)
```
## Hash Table Implementation

In Python, hash tables are implemented using dictionaries. Dictionaries are a collection of key-value pairs, where each key is unique. Here's a basic example of how to create and use a hash table (dictionary) in Python:

``` python
# Creating a dictionary (hash table)
hash_table = {}

# Adding key-value pairs
hash_table["key1"] = "value1"
hash_table["key2"] = "value2"

# Accessing values by key
value = hash_table["key1"]
print("Value for key1:", value)

# Checking if a key exists
if "key3" in hash_table:
    print("Key3 exists")
else:
    print("Key3 does not exist")
```
This README provides an overview of hash tables and how to use them in Python, including solving the first recurring character problem using a hash table and basic hash table implementation.

