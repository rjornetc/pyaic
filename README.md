# pyaic
Python Alphabetical Index Compressor is a Python3 module to compress strings by the index of each characters in a given Alphabet 

# Example
If we want to compress the string what we know can only have lowercase and space we can define our alphabet as:
```
ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
```
So, we can compress lowercase strings by using:
```
<<< import alphabetical_index_compesor as aic
<<< ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
<<< aic.compress('hello world', ALPHABET)
>>> 1318742925770068
<<< aic.decompress(1318742925770068, ALPHABET)
>>> 'hello world'
```
