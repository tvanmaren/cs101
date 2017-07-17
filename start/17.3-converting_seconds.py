# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(given):
    h_format="hours"
    m_format="minutes"
    s_format="seconds"
    try:
        remainder=given.split('.')
        remainder[1]=float(remainder[1])
    except:
        remainder=[0,0]
    hours=int(given/3600)
    minutes=int((given-(3600*hours))/60)
    seconds=(given-((3600*hours)+(60*minutes)))+(remainder[1]/10)
    if hours==1:
        h_format="hour"
    if minutes==1:
        m_format="minute"
    if seconds==1.0:
        return "%i %s, %i %s, %i second" % (hours,h_format,minutes,m_format,seconds)
    return "%i %s, %i %s, %.1f seconds" % (hours,h_format,minutes,m_format,seconds)

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds(1)