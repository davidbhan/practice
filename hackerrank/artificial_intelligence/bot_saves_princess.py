# https://www.hackerrank.com/challenges/saveprincess

DEBUG = False

def get_char_position(n, grid, char = 'm'):
    pos_x, pos_y = 0, 0
    for r in range(0,n):
        if char in grid[r]:
            bot_line = grid[r]
            for c in range(0,n):
                if bot_line[c] == char:
                    pos_x = c
                    break
            pos_y = r

    if DEBUG:
        print(char + ' at:' + str(pos_x) + ',' + str(pos_y))
        
    return pos_x, pos_y

def compute_shift(src_x, src_y, dest_x, dest_y):
    # positive shift for right and up
    shift_x = dest_x - src_x
    shift_y = src_y - dest_y
    
    if DEBUG:
        print('shift required:' + str(shift_x) + ',' + str(shift_y))
    
    return shift_x, shift_y

def shift_to_human_readable(shift_x, shift_y):
    output = ''
    
    while(shift_x != 0):
        if shift_x > 0:
            output += 'RIGHT\n'
            shift_x -= 1
        else:
            output += 'LEFT\n'
            shift_x += 1
            
    while(shift_y != 0):
        if shift_y > 0:
            output += 'UP\n'
            shift_y -= 1
        else:
            output += 'DOWN\n'
            shift_y += 1
    
    return output
    
def displayPathtoPrincess(n,grid):
    p_x, p_y = get_char_position(n, grid, 'p')
    m_x, m_y = get_char_position(n, grid, 'm')
    shift_x, shift_y = compute_shift(m_x, m_y, p_x, p_y)
    directions = shift_to_human_readable(shift_x, shift_y)
    print(directions)


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)