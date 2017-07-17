# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    return [match,replacement]



def apply_converter(converter, string):
    matchspot=0
    match=converter[0]
    replacement=converter[1]
    matchspot=string.find(match)
    while matchspot!=-1:
        print "match found at",string[matchspot-3:matchspot+3]
        string=string[:matchspot]+replacement+string[matchspot+len(match):]
        print "string converted to",string
        matchspot=string.find(match)
    return string


# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

c2=make_converter('&','and')
print apply_converter(c2,'The cat & the dog')

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).
