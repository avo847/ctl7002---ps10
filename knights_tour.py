import collections as coll
import numpy as np


    
class Board:
  """ Class to store data for a square chessboard of specified size (default 8x8)
  Data is stored as a list of point objects. The board can check to see whether a 
  particular point is in use or open
  
  Coordinates denote (row, col) and start at (0,0) in upper-left corner
  
  points are numpy.array objects with two elements
  """
  def __init__(self, size=8):
    self.spaces_used = np.array([ np.array([-1,-1]) ])
    self.size = size
  
  def is_valid(self, point):
    """ Check whether a particular point is on the board"""
    if point[0] < 0 or point[1] < 0:
      return False
    elif point[0] >= self.size or point[1] >= self.size:
      return False
    else:
      return True
      
      
  def is_free(self, point):
    """ Check whether a particular point is not already in movelist"""
    return (not point in self.spaces_used)
    
    
  def use_space(self, point):
    if self.is_free(point):
      self.spaces_used = np.append(self.spaces_used, [point], axis=0)
    else:
      print point,  " alread in use!"
    
    
    
class Knight:
  """ Class to store data for a kight moving allong chessboard
  Includes a list of moves the knight has taken as well as available moves 
  at each step. 
  
  The knight needs to "talk" to the board to know which spaces are available.
  It also needs to tell the board to update its list of used spaces after making a move.
  
  """
  def __init__(self, board, start_pos):
    self.moves = coll.OrderedDict()
    self.board = board
    self.board_size = board.size
    self.spaces_used = board.spaces_used
    self.current = start_pos
    self.add_move(self.current)

    
  def get_moves(self, point):
    poss_moves = []
    y_cur = point[0]
    x_cur = point[1]
    for x in [-1, 1]:
      for y in [-2, 2]:
        a = self.current + np.array([x,y])
        if self.board.is_valid(a): # add space to move list
          poss_moves.append(a)
    for x in [-2,2]:
      for y in [-1,1]: 
        a = self.current + np.array([x,y])
        if self.board.is_valid(a): # add space to move list
          poss_moves.append(a)
    
    return poss_moves
    

  def add_move(self, point):
    self.moves[point.tostring()] = self.get_moves(point)

    
  def print_move_list(self):
    for p in self.moves.keys():
      print "At ", np.fromstring(p, dtype=int), " possible moves are :"
      for q in self.moves[p]:
        print "  ", q
        
      
