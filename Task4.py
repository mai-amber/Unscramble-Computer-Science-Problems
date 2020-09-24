"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = []
ingoing_calls = []
outgoing_texts = []
ingoing_texts = []
telemarketers = []

for call in calls:
    outgoing = call[0]
    ingoing = call[1]

    if outgoing not in outgoing_calls:
        outgoing_calls.append(outgoing)
    if ingoing not in ingoing_calls:
        ingoing_calls.append(ingoing)

for text in texts:
    outgoing = text[0]
    ingoing = text[1]

    if outgoing not in outgoing_texts:
        outgoing_texts.append(outgoing)
    if ingoing not in ingoing_texts:
        ingoing_texts.append(ingoing)

for num in outgoing_calls:
    if (num not in ingoing_calls) and (num not in ingoing_texts) and (num not in outgoing_texts):
        telemarketers.append(num)

print("These numbers could be telemarketers: ")
print ('\n'.join(sorted(set(telemarketers))))
        
