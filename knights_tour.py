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
    return (not self.point_in_list(point))
    
  def point_in_list(self, point):
    for i in np.arange(0,self.spaces_used.shape[0],1):
      if np.all(point == self.spaces_used[i,:]):
        return True
    return False
    
    
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
    self.spaces_used = 0 #board.spaces_used
    self.current = start_pos
    self.add_move(self.current)

    
  def get_moves(self, point):
    """determine available moves from given space """
    poss_moves = []
    #y_cur = point[0]
    #x_cur = point[1]
    for x in [-1, 1]:
      for y in [-2, 2]:
        a = point + np.array([x,y])
        if self.board.is_valid(a) and self.board.is_free(a): # add space to move list
          poss_moves.append(a)

    for x in [-2,2]:
      for y in [-1,1]: 
        a = point + np.array([x,y])
        if self.board.is_valid(a) and self.board.is_free(a): # add space to move list
          poss_moves.append(a)
    
    return poss_moves
    
 
  
  def add_move(self, point):
    """Manually add a move
    Takes a point in the form of a numpy array"""
    self.moves[point.tostring()] = self.get_moves(point)
    self.board.use_space(point)
    self.spaces_used = self.spaces_used+1
    

    
  def print_move_list(self):
    for p in self.moves.keys():
      print "At ", np.fromstring(p, dtype=int), " possible moves are :"
      for q in self.moves[p]:
        print "  ", q
    print "total spaces used: ", self.spaces_used
        
  def hash(self, point):
    return point.tostring()
    
  def next_move(self):
    """Use first move available on list at current location;
    if move list is empty, backtrack"""
    
    while len(self.moves[self.current.tostring()]) == 0:
      print "empty move list at position ", self.current
      print "backtracking..."
      self.backtrack()
    
    target = self.moves[self.current.tostring()][0]
    self.current = target # updated position
    self.board.use_space(self.current)
    self.spaces_used = self.spaces_used + 1
    self.moves[self.current.tostring()] = self.get_moves(self.current)
    
    
  def backtrack(self):
    """use only when there are no available moves.
    move to previous location and delete top move in move list. Also
    delete last element in self.moves, a point with empty move list
    """
    self.moves.popitem()# pop last item in list, i.e., location where there are no moves
    self.current = np.fromstring(self.moves.keys()[len(self.moves.keys())-1], dtype=int)    # set current to last item
    print self.current
    print type(self.current)
    key = self.current.tostring()
    self.moves[key] = self.moves[key] [1:] #remove first move, already tried
    self.spaces_used = self.spaces_used - 1
    

    
class Knights_tour:
  def __init__(self, start_pos, max):
    self.board = Board()
    self.knight = Knight(self.board, start_pos)
    self.max_moves = max
    
  def run(self):
    i = 1 # first move is placing knight on the board
    while i < self.max_moves:
      if self.knight.spaces_used == 64:
        print "Completed tour!"
        break;
        
      self.knight.next_move()
      i = i + 1
    print "used ", i, " moves."
    print "knight covered ", self.knight.spaces_used, " spaces at end."