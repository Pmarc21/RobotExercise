# robot.py
MAX_X = 4
MAX_Y = 4
MIN_X = 0
MIN_Y = 0
DIRECTIONS = ['NORTH', 'SOUTH', 'EAST', 'WEST']

def place(phrase):
    inside = 0 #we assume that every time robot is outside of the table
    phrase = str(phrase)
    function_execute_splitted = phrase.split(' ')
    position = function_execute_splitted[1].split(',')
    if int(position[0]) <= MAX_X and int(position[0]) >= MIN_X and int(position[1]) <= MAX_Y and int(position[1]) >= MIN_Y and position[2] in DIRECTIONS:
        inside = 1 # if it's inside, OK. If not, inside = 0 anyway.
    return int(position[0]),int(position[1]),position[2],inside


def report():
    print(str(x)+','+str(y)+','+f)


def move(x,y,f):
    if f == 'NORTH' and y < MAX_Y:
        y += 1
    elif f == 'SOUTH' and y > MIN_Y:
        y -= 1
    elif f == 'EAST' and x < MAX_X:
        x += 1
    elif f == 'WEST' and x > MIN_X:
        x -= 1
    #else:
        #print ('There is no enough room')
    return x,y,f

def left(f):
    if f == 'NORTH':
        f = 'WEST'
    elif f == 'EAST':
        f = 'NORTH'
    elif f == 'SOUTH':
        f = 'EAST'
    elif f == 'WEST':
        f = 'SOUTH'
    else:
        print('The specified direction is not correct')
    return f

def right(f):
    if f == 'NORTH':
        f = 'EAST'
    elif f == 'WEST':
        f = 'NORTH'
    elif f == 'SOUTH':
        f = 'WEST'
    elif f == 'EAST':
        f = 'SOUTH'
    else:
        print('The specified direction is not correct')
    return f


def read_file():
    data = []
    try:
        testFile = open('test_data_1.txt', 'r')
        lines = testFile.readlines()
        for line in lines:
            data.append(line.strip('\n'))
        return data
    except IOError:
        print('There was an error opening the file!')
        return

if __name__ == "__main__":
    x = 0
    y = 0
    f = 'NORTH'
    placed = 0
    function_execute = read_file()
    for j in range(0,len(function_execute)):
        if placed == 1: #only if we have placed robot first, we can execute different functions
            if 'PLACE' in function_execute[j]:
                x,y,f,inside = place(function_execute[j])
                placed = inside
            elif function_execute[j] == 'REPORT':
                report()
            elif function_execute[j] == 'MOVE':
                x,y,f = move(x,y,f)
            elif function_execute[j] == 'LEFT':
                f = left(f)
            elif function_execute[j] == 'RIGHT':
                f = right(f)
        else: #if robot is not placed, we can only execute PLACE and REPORT
            if 'PLACE' in function_execute[j]:
                x,y,f,inside = place(function_execute[j])
                placed = inside
            elif function_execute[j] == 'REPORT':
                print('Not in place')