# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def tag_out(str1):
    tag_start=str1.find('<')
    tag_end=str1.find('>',tag_start+1)
    if tag_start!=-1 and tag_end!=-1:
        adjustment=str1[:tag_start]+' '+str1[tag_end+1:]
        dbl_checked=tag_out(adjustment)
        return dbl_checked
    else:
        return str1
        
            

def remove_tags(s1):
    adjusted_s1=tag_out(s1)
    split_list=adjusted_s1.split()
    return split_list
        


print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']