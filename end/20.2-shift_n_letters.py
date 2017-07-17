# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    new_letter=ord(letter)+n
    if (new_letter)>122:
        return chr((new_letter%122)+96)
    elif (new_letter)<97:
        return chr(122-(96-new_letter))
    return chr(ord(letter)+n)



#print shift_n_letters('s', 1)
#>>> t
#print shift_n_letters('s', 2)
#>>> u
#print shift_n_letters('s', 10)
#>>> c
#print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('a',-1)
print shift_n_letters('k',-12)