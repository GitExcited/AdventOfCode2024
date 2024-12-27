#Open input and create list
list1 = []
list2 = []
with open('../inputs/day01.txt') as f:
    for line in f:
        # Split input into two lists
        parts = line.split(' ')
        if len(parts)>3:
            list1.append(int(parts[0]))
            list2.append(int(parts[3]))

## PART I
#Sort each list
list1.sort()
list2.sort()
#Perform difference sum of each i element for list1[i] list2[i]
sum = 0
for i in range (0,len(list1)):
    sum+= abs(list1[i] - list2[i])
print(sum)

#PART II
score=0
for el in list1:
    print(el * list2.count(el))
    score+= el * list2.count(el)
print(score)


