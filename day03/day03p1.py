# day 3 part 1

answer = 0

with open("day03.txt", "r") as file:
    for line in file:
        line = line.strip() 
        index = 0
        while index < len(line):
            findIndex = line[index:].find("mul(")
            if findIndex == -1:
                break
            
            index += findIndex + 4

            first = 0
            second = 0
            while index < len(line) and line[index].isdigit():
                first = first * 10 + int(line[index])
                index += 1

            if index < len(line) and line[index] == ",":
                index += 1  
            
                while index < len(line) and line[index].isdigit():
                    second = second * 10 + int(line[index])
                    index += 1

                if index < len(line) and line[index] == ")":
                    answer += first * second  
            index += 1

print(answer)
        
