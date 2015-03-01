"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result = []
    for ind in range(len(line)):
        result.append(0)

    merged = list(result) # list for keeping track which tiles have been merged
        
    jind = 0 # index for result list
    for ind in range(len(line)):
        if line[ind] != 0:
            result[jind] = line[ind]
            if jind > 0 and result[jind] == result[jind-1] and merged[jind-1] != True:
                    result[jind-1] += result[jind] # merge tiles
                    result.pop(jind) # remove second of the merged numbers
                    result.append(0) # fill up list to former length
                    merged[jind-1] = True
                    jind -= 1
            jind += 1
       
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        # compute list of indices for initial tiles for each direction
        up_ind = [(0, j) for j in range(self._grid_width)]
        print up_ind
        down_ind = [(self._grid_height-1, j) for j in range(self._grid_width)]
        print down_ind
        left_ind = [(i, 0) for i in range(self._grid_height)]
        print left_ind
        right_ind = [(i, self._grid_width-1) for i in range(self._grid_height)]
        self._initial_tiles = {UP : up_ind, DOWN : down_ind, LEFT : left_ind, RIGHT : right_ind}
        TwentyFortyEight.reset(self)
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # list comprehension for creating grid
        self._grid = [[x * 0 for x in range(self._grid_width)] for x in range(self._grid_height)]
        TwentyFortyEight.new_tile(self) # first tile
        TwentyFortyEight.new_tile(self) # second tile

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_rep = ""
        for row in self._grid:
            grid_rep += str(row) + "\n"
            
        return grid_rep

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self._direction = direction
        tile_values =[]
        if self._direction == UP or self._direction == DOWN:
            for tile in self._initial_tiles[(self._direction)]:
                for step in range(self._grid_height):
#                    print tile
                    row = tile[0] + step * OFFSETS[(self._direction)][0]
                    col = tile[1] + step * OFFSETS[(self._direction)][1]
#                    print "Processing cell", (row, col), 
#                    print "with value", self._grid[row][col] 
                    tile_values.append(self._grid[row][col])
                print tile_values
                merged_tiles = merge(tile_values)
                print merged_tiles
                tile_values = []
                    
        else:
            for tile in self._initial_tiles[(self._direction)]:
                for step in range(self._grid_width):
#                    print tile
                    row = tile[0] + step * OFFSETS[(self._direction)][0]
                    col = tile[1] + step * OFFSETS[(self._direction)][1]
                    print "Processing cell", (row, col), 
                    print "with value", self._grid[row][col]   
                
#        for step in range(num_steps):
#        row = start_cell[0] + step * direction[0]
#        col = start_cell[1] + step * direction[1]
#        print "Processing cell", (row, col), 
#        print "with value", EXAMPLE_GRID[row][col]    
#            
            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tile_created = False
        empty_tile = False
        
        # check for empty tile
        for row in self._grid:
            if 0 in row:
                empty_tile = True
                break
        
        while tile_created == False and empty_tile == True:
            rnd_row = random.randrange(self._grid_height)
            rnd_col = random.randrange(self._grid_width)
            rnd = random.random()
            # when tile is 0, insert 2 or 4
            if self._grid[rnd_row][rnd_col] == 0:
                if  rnd <= 0.9:
                    self._grid[rnd_row][rnd_col] = 2
                else:
                    self._grid[rnd_row][rnd_col] = 4
                tile_created = True
            # check if an empty tile is left
            for row in self._grid:
                if 0 in row:
                    break
                else:
                    empty_tile = False
        
                

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._row = row
        self._col = col
        self._value = value
        # reduce self._row and self._col by 1, otherwise lsit index out of range
        self._grid[self._row-1][self._col-1] = self._value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        self._row = row
        self._col = col
        return self._grid[self._row-1][self._col-1]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

#grid = TwentyFortyEight(5, 4)
#print grid
#grid.set_tile(3, 3, 8)
#print grid
#grid.new_tile()
#print grid
#print grid.get_tile(3,3)
#print "UP"
#grid.move(UP)
#print "DOWN"
#grid.move(DOWN)
#print "LEFT"
#grid.move(LEFT)
#print "RIGHT"
#grid.move(RIGHT)
#print TwentyFortyEight.get_grid_height(grid)
#print TwentyFortyEight.get_grid_width(grid)
