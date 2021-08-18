"""
Given an unsigned integer, write a function that returns the number of '1' bits
that the integer contains (the
[Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight))

Examples:

- `hamming_weight(n = 00000000000000000000001000000011) -> 3`
- `hamming_weight(n = 00000000000000000000000000001000) -> 1`
- `hamming_weight(n = 11111111111111111111111111111011) -> 31`

Notes:

- "Unsigned Integers (often called "uints") are just like integers (whole
numbers) but have the property that they don't have a + or - sign associated
with them. Thus they are always non-negative (zero or positive). We use uint's
when we know the value we are counting will always be non-negative."
"""
def hamming_weight(n):
    # Your code here
    # args = n is a numeric value
    # function = hamming_weight
    # hamming weight is the number of 1's in the binary representation of n
    # return the hamming weight of n without using any built-in functions
    # (except for the built-in `bin` function)
    # return the hamming weight of n
    # expected
#     - `hamming_weight(n = 00000000000000000000001000000011) -> 3`
# - `hamming_weight(n = 00000000000000000000000000001000) -> 1`
# - `hamming_weight(n = 11111111111111111111111111111011) -> 31`

    # convert n to binary
    binary = bin(n)
    # convert binary to string
    binary_string = str(binary)
    # count the number of 1's in binary_string
    count = binary_string.count('1')
    return count


print(hamming_weight(n = 11111111111111111111111111111011))
print(hamming_weight(n = 67801234057))
print(hamming_weight(n = 11111111111111111111111111111011))

#DOESN'T WORK HAVE ZERO CLUE HOW TO DO IT
