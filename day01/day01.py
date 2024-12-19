# Part 1

lst1 = []
lst2 = []

with open('day01.txt', 'r') as file:
    for line in file:
        entry = line.strip().split()
        lst1.append(int(entry[0]))
        lst2.append(int(entry[1]))

lst1.sort()
lst2.sort()

answer = 0
for i in range(len(lst1)):
    answer += (abs(lst1[i] - lst2[i]))

# -------------------------------------------------------------
# Part 2

answer = 0

for num in lst1:
    answer += num * lst2.count(num)

print(answer)

