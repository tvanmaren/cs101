# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def unit_conversion(size,unit):
    units=[['k',2**10],['M',2**20],['G',2**30],['T',2**40]]
    for element in units:
        if element[0]==unit[0]:
            bits=float(element[1])
    if unit[1]=='B':
        bits=bits*8
    bits=bits*size
    return bits
    
def seconds_conversion(seconds):
    hours=int(seconds/3600)
    seconds-=hours*3600.
    minutes=int(seconds/60)
    seconds-=minutes*60.
    return hours,minutes,seconds
    
def format_time(hours,minutes,seconds):
    h_format='hours'
    m_format='minutes'
    if hours==1:
        h_format='hour'
    if minutes==1:
        m_format='minute'
    if seconds==1:
        return "%i %s, %i %s, 1 second" % (hours,h_format,minutes,m_format)
    
    return "%i %s, %i %s, %s seconds" % (hours,h_format,minutes,m_format,seconds)

def download_time(filesize, fsunit, bandwidth, bwunit):
    bandwidth=unit_conversion(bandwidth,bwunit)
    filesize=unit_conversion(filesize,fsunit)
    seconds_to_download=filesize/bandwidth
    hours,minutes,seconds=seconds_conversion(seconds_to_download)
    return format_time(hours,minutes,seconds)



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB',5,'MB')
