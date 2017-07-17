# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(l1):
    if not l1:
        return None
    counter=1
    results=[]
    i=0
    for i in range(1,len(l1)):
        if l1[i-1]==l1[i]:
            counter+=1
        elif l1[i-1]!=l1[i]:
            results.append([l1[i-1],counter])
            counter=1
    results.append([l1[i],counter])
    number=None
    maximum=0
    print "processing",results
    for i in range(0,len(results)):
        if maximum<results[i][1]:
            maximum=results[i][1]
            number=results[i][0]
    return number
    




#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([2])

