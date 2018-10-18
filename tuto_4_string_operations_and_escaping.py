# Escaping
phrase = "Best \"Coder"

# Using lower and concatenation - careful with spaces
print(phrase.lower() + " is me")

# Using formatting and placeholders for concatenation
greeting = "Hello"
name = "Andrei"
welcome_message = "{}, {}. Welcome!".format(greeting, name)
print(welcome_message)

# Using the f function for concatenation and operation on strings
welcome_message = f"{greeting}, {name.upper()}. Welcome!"
print(welcome_message)

# Using upper and boolean isuper
print(phrase.upper().isupper())

# Using len
print(len(phrase))

# Using index of a character
print(phrase[3])

# Using two indexes, the first value (0) is included, the second value (3) is not !!!!!!
print(phrase[3:])

# Using index of a text
print(phrase.index("Bes"))

# Using replace - replaces a certain text with
print(phrase.replace("Coder", "Man"))

# Using triple quotes for return to line
message = """Bobby's world was a good 
cartoon in the 1990s"""
print(message)

# Using count - counts the number of occurrences
print(message.count("l"))

# Using find - finds the index of a certain letter
print(message.find("l"))

# Using dir function in order to find out all the methods and attributes available in Python on a given variable
print(dir(message))

# Using the help function in order to find out what exactly an attribute or a method does
print(help(str.lower()))
