"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
times = dict()
longest = calls[0][0]

for call in calls:
    caller = call[0]
    receiver = call[1]
    duration = call[3]

    if caller in times:
        times[caller] += int(duration)
    else:
        times[caller] = int(duration)

    if times[caller] > times[longest]:
        longest = caller

    if receiver in times:
        times[receiver] += int(duration)
    else:
        times[receiver] = int(duration)

    if times[receiver] > times[longest]:
        longest = receiver

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest, times[longest]))
