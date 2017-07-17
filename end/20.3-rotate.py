# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    new_letter=ord(letter)+n
    if (new_letter)>122:
        return chr((new_letter%122)+96)
    elif (new_letter)<97:
        return chr(122-(96-new_letter))
    return chr(ord(letter)+n)

def rotate(string1, n):
    result=''
    for i in range(0,len(string1)):
        if string1[i]==' ':
            result+=' '
        else:
            result+=shift_n_letters(string1[i],n)
    return result
    

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???