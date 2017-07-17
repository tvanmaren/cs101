# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def isleapyear(year):
    if year%4==0:
        if year%400==0:
            return True
        elif year%100==0:
            return False
        else:
            return True
    else:
        return False

def dayssinceyearstart(year,month):
    daysofmonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    daycount=0
    while month>0:
        daycount=daycount+daysofmonth[month-1]
        if isleapyear(year) and month==2:
            daycount=daycount+1
        month=month-1
    return daycount

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daysofmonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    daycount=day2
    month2=month2-1
    while year2>year1:
        daycount=daycount+dayssinceyearstart(year2, month2)
        year2=year2-1
        month2=12
    if year2==year1:
        while month2>month1:
            if isleapyear(year2) and month2==2:
                daycount=daycount+1
            daycount=daycount+daysofmonth[month2-1]
            month2=month2-1
        if month2==month1:
            daycount=daycount+(daysofmonth[month2-1]-day1)
            if isleapyear(year2) and month2==2:
                daycount=daycount+1
    else:
        return -1
    return daycount


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
print daysBetweenDates(2012,1,1,2012,2,28)
print daysBetweenDates(2012,1,1,2012,3,1)
print daysBetweenDates(2011,6,30,2012,6,30)
print daysBetweenDates(2011,1,1,2012,8,8)
print daysBetweenDates(1900,1,1,1999,12,31)