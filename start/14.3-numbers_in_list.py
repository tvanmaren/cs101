# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    numlist=[]
    sublist=[]
    cindex=0
    pindex=0
    while cindex<len(string):
        previous=int(string[pindex])
        current=int(string[cindex])
        # print "pindex,cindex:",pindex,cindex
        # print "previous,current:",previous,current
        pindex=cindex
        cindex+=1
        if not sublist:
            if previous>=current and pindex!=0: #avoids getting a false positive at the start of the string, where previous and current are both the first piece
                sublist.append(current)
                threshhold=previous
                # print "threshhold set at",threshhold
                # print "sublist set at",sublist
                continue #skip over sublist routines until we've moved to the next numbers
            else:
                numlist.append(current)
                # print "numlist set at",numlist
        if sublist:
            if current>threshhold:
                numlist.append(sublist)
                numlist.append(current)
                # print "numlist set at",numlist
                sublist=[]
                # print "sublist reset"
            if current<=threshhold:
                sublist.append(current)
                # print "sublist continued with",sublist
    if sublist and cindex==len(string): #if the threshhold wasn't met, but we hit the end of the string
        numlist.append(sublist)
        # print "numlist set at",numlist
    # print numlist
    return numlist


#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
