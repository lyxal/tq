# tq
In the language, every sequence of items make up a meta-list; the meta-list may be accessed arbitarily. (This language is inspired by [Jo King's Symbolic Raku quine.](https://codegolf.stackexchange.com/questions/69/golf-you-a-quine-for-great-good/197574#197574))
# Non-cheating Quine program
```
etq"etq"
```
# Explanation
```
   'etq' # Define the second item of the list
         # As a string
  q      # Surround the string with quotes
 t       # For the first item of the list,
         # Access the last (tail) item in the list,
e        # and evaluate the accessed value.

# The list becomes et,q'etq' (comma is for readability)
# , which then becomes foreach-printed without any separator.
```
# Hello, World! [works up to here]
It's just a boring indexing of the string "Hello, World!".
```
"Hello, World!"
```
# Explanation
```
"Hello, World!" # Make this string invisible in the final output
                # Access the first string in the list
```
In fact there is a shorthand for accessing the first item in the list. ```|```
# Cat program
```
!?~|
```
# Explanation
```
 ?   # Take a string from the input
!    # Make the string invisible in the final output
   | # Take the input
  ~  # Transpose the input by the first dimension
   
```
# Fibonacci sequence
```
11+|.2)
```
# Explanation
```
11      # Define the first 2 items in the infinite list: 1 and 1
  +|.2  # Define the 3rd item as list item 1 plus list item 2
      ) # Extend the list forever
```
# Truth machine
```
?'|x)
```
# Explanation
```
?     # Define the first item as an item from input
  |   # Index the first item in the list
 ' x  # OR it with a nil value (which auto-implies)
      # deletion of the current cell.
      # To actually store a nothing value in the current
      # cell, use the null (l) value.
    ) # Extend the current list forever
```
# Infinite loop producing no output
```
l)
```
# Explanation
```
l  # Set the current item to the null value
   # (this does not contribute to the output)
 ) # Extend the list forever based on the previous pattern
```
# Prime tester
```
?'%|.2x)
```
