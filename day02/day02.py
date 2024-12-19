# Part 1

entries = []

with open('day02.txt', 'r') as file:
    for line in file:
        entries.append([int(i) for i in line.strip().split()])

count = 0
for entry in entries:
    if entry == sorted(entry):
        valid = True
        for i in range(0, len(entry) - 1):
            if (entry[i + 1] - entry[i]) > 3 or (entry[i + 1] - entry[i]) < 1:
                valid = False
                break
        if valid:
            count += 1

    entry.reverse()
    if entry == sorted(entry):
        newentry = sorted(entry)
        valid = True
        for i in range(0, len(newentry) - 1):
            if (newentry[i + 1] - newentry[i]) > 3 or (newentry[i + 1] - newentry[i]) < 1:
                valid = False
                break
        if valid:
            count += 1
        
# -------------------------------------------------------------
# Part 2

def checkSafe(entry):
    if entry == sorted(entry):
        for i in range(0, len(entry) - 1):
            if (entry[i + 1] - entry[i]) > 3 or (entry[i + 1] - entry[i]) < 1:
                return False
        return True

    entry.reverse()
    if entry == sorted(entry):
        for i in range(0, len(entry) - 1):
            if (entry[i + 1] - entry[i]) > 3 or (entry[i + 1] - entry[i]) < 1:
                return False
        return True
    
    return False

def bufferCheck(entry):
    for i in range(len(entry)):
        if checkSafe(entry[0:i] + entry[i + 1:]):
            return True
    return False

count = 0
for entry in entries:
    if checkSafe(entry) or bufferCheck(entry):
        count += 1


print(count)