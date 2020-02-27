# https://www.hackerrank.com/challenges/botcleanr
DEBUG = False

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

    if DEBUG:
        print('closest pos:' + str(next_x) + ',' + str(next_y))

    directions = shift_to_human_readable(shift_x, shift_y)
    print(directions.partition('\n')[0])
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)