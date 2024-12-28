#Create is_safe() method
def is_safe(line):
    if line[0] > line[1]: #must be in decreasing scenario
        for i in range (0, len(line) - 1):
            if line[i]<=line[i+1] or line[i]-3 > line[i+1]:
                return False
        return True
    elif line[0] < line[1]:#must be in increasing scenario
        for i in range (0, len(line) - 1):
            if line[i]>=line[i+1] or line[i]+3 < line[i+1]:
                return False
        return True
    return False

#Open file and
with open('../inputs/day02.txt') as f:
    count = 0
    for line in f:
        array=line.strip().split(' ')
        numbers=[int(x) for x in array]
        if is_safe(numbers):
            count += 1
    print(count)


# TESTING
with open('../tests/day02.txt') as t:
    for line in t:
        array = line.strip().split(' ')
        numbers = [int(x) for x in array]
        # print(is_safe(numbers))

#PART II
#create new is_safe_asc and is_safe_desc methods which check only pairs of elements
def is_safe_asc(pair):
    if pair[0] < pair[1] <= pair[0] + 3:
        return True
    return False
def is_safe_desc(pair):
    if pair[0] > pair[1] >= pair[0] -3:
        return True
    return False
def is_damp_safe(n,func):
    for i in range(0, len(n) - 1):
        #func lets us check ascending or descending as a parameter
        if not func( n[i:i + 2] ):
            # failure found. check if removing i or i+1 makes it safe
            # remove i element
            temp1= n[:i] + n[i+1:]
            # remove i+1 element
            if i==len(n)-2:
                temp2= n[:i+1] # edge case: we are at the before last element
            else:
                temp2= n[:i+1] +n[i+2:]
            if is_safe(temp1) or is_safe(temp2):
                return True
            return False
    return True


#open file and determine if line is asc or desc
with open('../inputs/day02.txt') as f:
    count=0
    for l in f:
        line= l.strip().split(' ')
        numbers = [int(x) for x in line]
        #Check if numbers are safe in descending or ascending order
        if is_damp_safe(numbers,is_safe_asc) or is_damp_safe(numbers,is_safe_desc):
            count+=1
    print('damp safe = '+str(count))



