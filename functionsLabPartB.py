# Problem 1: Using Default Parameters
# Write a function called 'introduce_yourself' that takes two parameters: 'name' and 'age'.
# The 'age' parameter should have a default value of 18.
# The function should print "Hello, my name is {name} and I am {age} years old." 
# Test the function by calling it with different arguments, including just providing a name.





# Problem 2: Variable-Length Arguments (*args) and multiple returns
# Write a function called 'sum_avg_of_numbers' that accepts a variable number of arguments using *args.
# The function should return the sum and average of all the numbers passed to it.
# Test the function with different numbers of arguments.






# Problem 3: Variable-Length Arguments (*args) with Keyword argument
# Write a function called 'combine_strings' that takes a separator string and an arbitrary number 
# of strings using *args. The function should return a single string combining all the input 
# strings, separated by the separator. (No seperator at the start or end
# Tests are given below



print(f"{combine_strings('one', 'two', 'three', sep='*') = }")
print(f"{combine_strings('po', 'ta', 'to', sep='~') = }")
print(f"{combine_strings('G', 'R', 'E', 'A', 'T', sep=' ') = }")
print(f"{combine_strings('Sleep', 'Eat', 'Greet', 'Bleet', 'Sheep', sep='ing ') = }")
