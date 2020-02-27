# https://www.hackerrank.com/challenges/botcleanlarge
def get_multiple_char_positions(num_rows, num_columns, grid, char = 'd'):
    positions =[]
    row, col = 0, 0
    for r in range(0, num_rows):
        if char in grid[r]:
            bot_line = grid[r]
            for c in range(0, num_columns):
                if bot_line[c] == char:
                    positions.append( (r, c) )

    return positions

def compute_shift(src_r, src_c, dest_r, dest_c):
    shift_r = dest_r - src_r
    shift_c = dest_c - src_c
    
    return shift_r, shift_c

def shift_to_human_readable(shift_r, shift_c):
    output = ''
    
    while(shift_r != 0):
        if shift_r > 0:
            output += 'DOWN\n'
            shift_r -= 1
        else:
            output += 'UP\n'
            shift_r += 1
            
    while(shift_c != 0):
        if shift_c > 0:
            output += 'RIGHT\n'
            shift_c -= 1
        else:
            output += 'LEFT\n'
            shift_c += 1
    
    output += 'CLEAN\n'

    return output

def next_move(posx, posy, dimx, dimy, board):
    num_rows, num_columns = dimx, dimy
    bot_row, bot_col = posx, posy

    positions = get_multiple_char_positions(num_rows, num_columns, board, 'd')

    next_r, next_c = positions[0]
    shift_r, shift_c = compute_shift(bot_row, bot_col, next_r, next_c)
    closest_distance = abs(shift_r) + abs(shift_c)
    for r, c in positions:
        d_r, d_c = compute_shift(bot_row, bot_col, r, c)
        distance = abs(d_r) + abs(d_c)
        if distance <= closest_distance:
            closest_distance = distance
            next_r, next_c = r, c
            shift_r, shift_c = compute_shift(bot_row, bot_col, next_r, next_c)

    directions = shift_to_human_readable(shift_r, shift_c)
    print(directions.partition('\n')[0])

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)