## Adventures of Coding 2023
## Day 1: 2023-12-01
## Robert Eckman

## Disclaimer: I'm doing this to improve my coding skills, but I am also taking advantage of tools made avalible to me.

## Did not start until 2023-12-04 11:30 pm or so

## Use Regular Expressions to find first digit and last digit in from a string and convert them into two-digit number. 
## Note, the last char might not be a digit, so you need to find the first digit from the left and the first digit from the right.
## Example: "A4B6C8D3" -> 43
## Example: "A4B6C8j" -> 48

import re                                           # Regular Expressions library

def find_first_and_last_digit(string):
    first_digit = re.search(r'\d', string).group()      # this works fine
    last_digit = re.findall(r'\d', string)[-1]          # corrected syntax
    return int(first_digit + last_digit)

print(find_first_and_last_digit("A4B6C8D3"))        # This works fine, returns 43
print(find_first_and_last_digit("A4B6C8DJ"))        # This was causing an error because last char is not a digit

## TODO: allow input from file (input.raw)

## TODO: convert the find_first_and_last_digit function to return an integer instead of a string

## TODO: sum all the integers in the input.raw file based on the rules of the find_first_and_last_digit function

