import re

def multiply(content):
    matches = re.findall(r"mul\((\d+),(\d+)\)",
                         content)  # Looks for pattern mul( digit(s) , digit(s)  ) where x,y are stored tuples
    tuples = [(int(x), int(y)) for x, y in matches]
    sum = 0
    for t in tuples:
        sum += t[0] * t[1]
    return sum
#PART I
with open("../inputs/day03.txt") as f:
    content = f.read()
    sum=multiply(content)

#PART II
with open ("../inputs/day03.txt") as file:
    content= file.read()
    #start with empty array
    segments=[]
    flag = True
    i=0
    j=0
    while i<len(content):
    #LOOP: i = 0
        if flag and content.startswith("don't()",i):
            # if you find a dont(), add elements from [j, dont()] to the empty array. put up flag
            segments.append(content[ j : i ])
            flag = False
            # keep reading until you find a do
        elif not flag and content.startswith("do()",i):
            # when you find do, set j to position of i, lower flag
            j=i
            flag = True
        i+=1
    # when reaching end of string, add elements from i to end if flag up. otherwise dont add them
    if flag:
        segments.append(content[ j : i ])
    clean_content= ''.join(segments)
    print(multiply(clean_content))


