# Mystery-language
In the language, every sequence of items make up a meta-list; the meta-list may be accessed arbitarily.
# Non-cheating Quine program
```
.2".2"
```
# Explanation
```
.2     # We index into the main list
       # and select the second item
       # of the string into this index
       # Now we are starting a new item
       # of the meta-list.
  ".2" # This is just a string describing
       # the first part of the list.
       # Then, the list is implicitly outputted
       # without any delimiters.

# Our constructed list is [a[2],".2"], which
# turns into .2, ".2". The string is outputted
# as-is, therefore the output is .2".2".
```
# Hello, World!
It's just a boring indexing of the string "Hello, World!".
```
!"Hello, World!".1
```
# Explanation
```
!"Hello, World!"   # Make this string invisible in the final output
                .1 # Access the first string in the list
```
