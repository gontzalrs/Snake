
from copy import deepcopy


def numberOfAvailableDifferentPaths(board, snake, depth):
    """Returns the available number of Paths for the given snake on the given board, 
    for as many steps as depth.
    
    Parameters
    ----------
    board : 2-dimensional array of integers
        Dimensions of the board -> [rows, columns].
    snake : array of 2-dimensional arrays 
        Position of each snake bodypart on the board.
        3 <= snake length <= 7
    depth : integer
        Number of steps that the path has to take.
        1 <= depth <= 20
    """
   
    return sumAvailableDifferentPaths(board, snake, depth, "N")

def sumAvailableDifferentPaths(board, snake, depth, previousMovement):
    """Recursively calls this same function for all the cases where the 
    snake can move, reducing depth in 1, and adds up all valid paths for
    each direction.

    When depth equals 0, it means that the snake is able to make the current 
    path and 1 is returned.
    
    Parameters
    ----------
    board : 2-dimensional array of integers
        Dimensions of the board -> [rows, columns].
    snake : array of 2-dimensional arrays 
        Position of each snake bodypart on the board.
        3 <= snake length <= 7
    depth : integer
        Number of steps that the path has to take.
        1 <= depth <= 20
    previousMovement : direction of the movement just done.
        Its value is L if previous movement was to the left, R if right,
        U if up and D if down. It can also be N (refering to None) for the 
        first call of the function.
    """
    if depth == 0:
        return 1

    leftSum = 0
    if previousMovement != "R" and tryLeft(snake) == True:
        #Creates a copy of the snake after it moves left
        newSnake = [snake[0].copy()] + deepcopy(snake)[:-1]
        newSnake[0][1] = newSnake[0][1]-1
        leftSum = sumAvailableDifferentPaths(board, newSnake, depth-1, "L")
    
    upSum = 0
    if previousMovement != "D" and tryUp(snake) == True:
        #Creates a copy of the snake after it moves up
        newSnake = [snake[0].copy()] + deepcopy(snake)[:-1]
        newSnake[0][0] = newSnake[0][0]-1
        upSum = sumAvailableDifferentPaths(board, newSnake, depth-1, "U")

    rightSum = 0
    if previousMovement != "L" and tryRight(board[1]-1 , snake) == True:
        #Creates a copy of the snake after it moves right
        newSnake = [snake[0].copy()] + deepcopy(snake)[:-1]
        newSnake[0][1] = newSnake[0][1]+1
        rightSum = sumAvailableDifferentPaths(board, newSnake, depth-1, "R")

    downSum = 0
    if previousMovement != "U" and tryDown(board[0]-1, snake) == True:
        #Creates a copy of the snake after it moves down
        newSnake = [snake[0].copy()] + deepcopy(snake)[:-1]
        newSnake[0][0] = newSnake[0][0]+1
        downSum = sumAvailableDifferentPaths(board, newSnake, depth-1, "D")
    
    return leftSum+upSum+rightSum+downSum

def selfIntersects(snake, nextHeadPosition):
    """Checks whether the snake would collide with itself or not.

    Parameters
    ----------
    snake : array of 2-dimensional arrays 
        Position of each snake bodypart on the board.
        3 <= snake length <= 7
    nextHeadPosition : 2-dimensional array of integers
        Position the head of the snake is attempting to take.
    """
    # Last element of the list will be ignored since the tail will get out of
    # its current position
    for bodyPartPosition in snake[1:-1]: 
        if nextHeadPosition == bodyPartPosition:
            return True
    
    return False

def tryLeft(snake):
    """Try of a movement to the left by the snake head. If it can be done, 
    return TRUE

    Parameters
    ----------
    board : 2-dimensional array of integers
        Dimensions of the board -> [rows, columns].
    snake : array of 2-dimensional arrays 
        Position of each snake bodypart on the board.
        3 <= snake length <= 7    
    """
    # This If checks whether the snake will get out of borders or not
    if snake[0][1] == 0:
        return False
    
    # Now the self intersection will be checked, using next head position
    nextHeadPosition = snake[0].copy()
    nextHeadPosition[1] = nextHeadPosition[1]-1
    return not selfIntersects(snake, nextHeadPosition)

def tryUp(snake):
    """Try of a movement to the left by the snake head. If it can be done, 
    return TRUE

    Parameters
    ----------
    board : 2-dimensional array of integers
        Dimensions of the board -> [rows, columns].
    snake : array of 2-dimensional arrays 
        Position of each snake bodypart on the board.
        3 <= snake length <= 7    
    """
    # This If checks whether the snake will get out of borders or not
    if snake[0][0] == 0:
        return False
    
    # Now the self intersection will be checked, using next head position
    nextHeadPosition = snake[0].copy()
    nextHeadPosition[0] = nextHeadPosition[0]-1
    return not selfIntersects(snake, nextHeadPosition)

def tryRight(lastColumnIndex, snake):
    """Try of a movement to the right by the snake head. If it can be done, 
    return TRUE

    Parameters
    ----------
    lastColumnIndex : index of the the last column of the board
        For example, for a [3,6] board, the index of the last column would be 5.
    snake : array of 2-dimensional arrays 
        Position of each snake bodypart on the board.
        3 <= snake length <= 7    
    """
    # This If checks whether the snake will get out of borders or not
    if snake[0][1] == lastColumnIndex:
        return False
    
    # Now the self intersection will be checked, using next head position
    nextHeadPosition = snake[0].copy()
    nextHeadPosition[1] = nextHeadPosition[1]+1
    return not selfIntersects(snake, nextHeadPosition)

def tryDown(lastRowIndex, snake):
    """Try of a movement to the left by the snake head. If it can be done, 
    return TRUE

    Parameters
    ----------
    lastRowIndex : index of the the last row of the board
        For example, for a [3,6] board, the index of the last row would be 2.
    snake : array of 2-dimensional arrays 
        Position of each snake bodypart on the board.
        3 <= snake length <= 7    
    """
    # This If checks whether the snake will get out of borders or not
    if snake[0][0] == lastRowIndex:
        return False
    
    # Now the self intersection will be checked, using next head position
    nextHeadPosition = snake[0].copy()
    nextHeadPosition[0] = nextHeadPosition[0]+1
    return not selfIntersects(snake, nextHeadPosition)

# These 3 lines test the code with the given acceptance tests
print("Should be 7 -> ", numberOfAvailableDifferentPaths([4, 3], [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]], 3))    
print("Should be 1 -> ", numberOfAvailableDifferentPaths([2, 3], [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]], 10))    
print("Should be 81 -> ", numberOfAvailableDifferentPaths([10, 10], [[5,5], [5,4], [4,4], [4,5]], 4))    