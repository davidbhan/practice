# https://www.hackerrank.com/challenges/botclean
DEBUG = True

def get_multiple_char_positions(n, grid, char = 'd'):
    positions =[]
    pos_x, pos_y = 0, 0
    for r in range(0,n):
        if char in grid[r]:
            bot_line = grid[r]
            for c in range(0,n):
                if bot_line[c] == char:
                    positions.append( (c, r) )
            
    if DEBUG:
        print(char + ' at:' + str(positions))

    return positions

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
    
    output += 'CLEAN\n'

    return output

def next_move(posr, posc, board):
    positions = get_multiple_char_positions(5, board, 'd')
    m_x, m_y = posc, posr

    next_x, next_y = positions[0]
    shift_x, shift_y = compute_shift(m_x, m_y, next_x, next_y)
    closest_distance = abs(shift_x) + abs(shift_y)
    for x, y in positions:
        d_x, d_y = compute_shift(m_x, m_y, x, y)
        distance = abs(d_x) + abs(d_y)
        if distance < closest_distance:
            closest_distance = distance
            next_x, next_y = x, y
            shift_x, shift_y = compute_shift(m_x, m_y, next_x, next_y)


    if DEBUG:
        print('closest pos:' + str(next_x) + ',' + str(next_y))

    directions = shift_to_human_readable(shift_x, shift_y)
    print(directions.partition('\n')[0])

if __name__ == "__main__":
    pos = '''0 0'''
    board0 = '''
bd---
-d---
---d-
---d-
--d-d
        '''

    board1 = '''
b--d-
ddd--
-----
-----
d-d--
        '''

    board2 = '''
d---d
-d---
--dd-
--dd-
dd--d
        '''

    pos = [int(i) for i in pos.strip().split()]
    board = [j for j in board1.strip().split('\n')]
    next_move(pos[0], pos[1], board)