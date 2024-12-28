
#create function which returns the digits bottom, right, left, up, and each diagonal
def get_words(direction):
    if direction == 'N':
        pass
    elif direction =='S':
        pass
    elif direciton == 'E':
        pass
    elif direction == 'W':
        pass
    elif direction =='NE':
    elif direction == ''

with open('../inputs/day04.txt') as f:
    lines = []
    for line in f:
        # open the file as a 2d Array
        lines.append([char for char in line.strip()])
    print(lines[0])

#Find edge cases for when checking in certain directions isn't necessary
#check each index looking for an X. when x, found, look in each direction for [X,M,A,S]
#count ++ when found