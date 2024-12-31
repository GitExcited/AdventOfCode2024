import itertools

#Turns an input direction like 'NE' to its vector (1,1)
def directions_to_vector(directions):
    directions_1 =['N','S']
    directions_2 =['E','W']
    vector_directions = [1,-1]
    vector =[0,0]
    for d in directions:
        if d in directions_1:
            vector[0]= vector_directions[directions_1.index(d)]
        elif d in directions_2:
            vector[1]= vector_directions[directions_2.index(d)]
    return vector
#create function which returns the digits bottom, right, left, up, and each diagonal
def get_word(direction, start):
    vector = directions_to_vector(direction)
    i = -vector[0]
    j = vector[1]
    word = []
    for k in range (0,4):
        word.append( lines[start[0]+(k*i)][start[1]+(k*j)] )
    return word

def is_target(word):
    if word ==target:
        return 1
    else:
        return 0



with open('../inputs/day04.txt') as f:
    lines = []
    iterations =0
    target =['X','M','A','S']
    for line in f:
        # open the file as a 2d Array
        lines.append([char for char in line.strip()])
    print(lines[1])
    for line in lines:
        print (len(line))
    count= 0
    for i in range (0,len(lines)):
        for j in range(0,len(lines[0])):
            dir1 = ['N', 'S']
            dir2 = ['E', 'W']
            #check if this is an X, obviously can't create a XMAS without starting with an X, cuts number of iterations
            if not lines[i][j] =='X':
                continue
            if i<3:
                dir1.remove('N')
            if i> len(lines)-4:
                dir1.remove('S')
            if j<3:
                dir2.remove('W')
            if j> len(lines[0])-4:
                dir2.remove('E')
            cross_product = list(itertools.product(dir1, dir2))
            start = (i,j)
            for direction in dir1:
                count+= is_target(get_word(direction,start))
            for direction in dir2:
                count+= is_target(get_word(direction,start))
            for direction in cross_product:
                count += is_target(get_word(direction, start))
    print(count)
    print(iterations)

#Find edge cases for when checking in certain directions isn't necessary
#check each index looking for an X. when x, found, look in each direction for [X,M,A,S]
#count ++ when found