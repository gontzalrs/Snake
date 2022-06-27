




def numberOfAvailableDifferentPaths(board, snake, depth):
    """Returns the available number of Paths for the given snake on the given board, 
    for as many steps as depth.
    
    Parameters
    ----------
    board : 2-dimensional array of integers
        Dimensions of the board -> [rows, columns].
    snake : array of 2-dimensional arrays 
        Position of each snake bodypart on the board.
        3 >= snake length >= 7
    depth : integer
        Number of steps that the path has to take.
"""