
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
   
    return sumAvailableDifferentPaths(board, snake, depth)

def sumAvailableDifferentPaths(board, snake, depth):
    if depth == 0:
        return 1

    leftSum = 0
    a = tryLeft(snake)
    if tryLeft(snake) == True:
        newSnake = [snake[0].copy()] + deepcopy(snake)[:-1]
        newSnake[0][1] = newSnake[0][1]-1
        leftSum = sumAvailableDifferentPaths(board, newSnake, depth-1)
    
    upSum = 0
    if tryUp(snake) == True:
        newSnake = [snake[0].copy()] + deepcopy(snake)[:-1]
        newSnake[0][0] = newSnake[0][0]-1
        upSum = sumAvailableDifferentPaths(board, newSnake, depth-1)

    rightSum = 0
    if tryRight(board[1]-1 , snake) == True:
        newSnake = [snake[0].copy()] + deepcopy(snake)[:-1]
        newSnake[0][1] = newSnake[0][1]+1
        rightSum = sumAvailableDifferentPaths(board, newSnake, depth-1)

    downSum = 0
    if tryDown(board[0]-1, snake) == True:
        newSnake = [snake[0].copy()] + deepcopy(snake)[:-1]
        newSnake[0][0] = newSnake[0][0]+1
        downSum = sumAvailableDifferentPaths(board, newSnake, depth-1)
    
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
    if snake[0][1] == 0:
        return False
    
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
    if snake[0][0] == 0:
        return False
    
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
    if snake[0][1] == lastColumnIndex:
        return False
    
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
    if snake[0][0] == lastRowIndex:
        return False
    
    nextHeadPosition = snake[0].copy()
    nextHeadPosition[0] = nextHeadPosition[0]+1
    return not selfIntersects(snake, nextHeadPosition)


print("numberOfAvailableDifferentPaths = ")    
print(numberOfAvailableDifferentPaths([2, 3], [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]], 10))