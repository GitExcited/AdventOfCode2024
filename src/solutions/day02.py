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
def is_damp_safe(n):
    #TODO: determine if list should be ascending or descending
    if n[0] > n[1] or n[1] > n[2]:
        func = is_safe_asc
    else:
        func = is_safe_desc
    for i in range(0, len(n) - 1):
        if not func( n[i:i + 2] ):
            # failure found. edge case one is failure at first two elements
            if i == 0:
                # case 1: does removing element 0 make it safe?
                if is_safe( n[1:] ):
                    pass

            # case 2: does removing element 1 make it safe?
#open file and determine if line is asc or desc
with open('../inputs/day02.txt') as f:
    count=0
    for l in f:
        line= l.strip().split(' ')
        numbers = [int(x) for x in line]
        if is_damp_safe(numbers):
            count+=1


#check pair by pair until failure. at failure create two possible scenarios.
# if either succeeds AND the remaining succeds then accept. otherwise reject
