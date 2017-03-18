import collections as coll
import numpy as np
import pdb
    
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
    #else:
      #print point,  " alread in use!"
      
  def free_space(self,point):
    if not self.is_free(point):
      #self.spaces_used = np.delete(self.spaces_used, point, 0) # here lies the problem
      self.spaces_used = self.spaces_used[:len(self.spaces_used)-1] #remove last element
      
    
    
    
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
    np.random.seed(11)
    
  def get_moves(self, point, warnsdorf=True):
    """determine available moves from given space """
    poss_moves = []
 
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
    #np.random.shuffle(poss_moves)
    
    """If warnsdorf=True, use Warnsdorf's heuristic, picking the point that has 
    fewest available moves. """
    if warnsdorf:
      poss_moves = sorted(poss_moves, key=self.how_many)
      
      
    return poss_moves
    
  def how_many(self, point):
    """determine how many moves can be made from a given point."""
    n_moves=0
    for x in [-1, 1]:
      for y in [-2, 2]:
        a = point + np.array([x,y])
        if self.board.is_valid(a) and self.board.is_free(a): # add space to move list
          n_moves+=1

    for x in [-2,2]:
      for y in [-1,1]: 
        a = point + np.array([x,y])
        if self.board.is_valid(a) and self.board.is_free(a): # add space to move list
          n_moves+=1
    #np.random.shuffle(poss_moves)
    return n_moves
    
    
  
  def add_move(self, point):
    """Manually add a move
    Takes a point in the form of a numpy array"""
    self.moves[point.tostring()] = self.get_moves(point)
    self.board.use_space(point)
    self.spaces_used = self.spaces_used+1
    

    
  def print_move_list(self):
    n = 1
    for p in self.moves.keys():
      print n, " : at ", np.fromstring(p, dtype=int), " possible moves are :"
      for q in self.moves[p]:
        print "  ", q
      n = n+1
    print "total spaces used: ", self.spaces_used
        
  def hash(self, point):
    return point.tostring()
    
  def next_move(self):
    """Use first move available on list at current location;
    if move list is empty, backtrack"""
    
    while len(self.moves[self.current.tostring()]) == 0:
      self.backtrack()
    
    target = self.moves[self.current.tostring()][0] # a numpy array
    self.board.use_space(target) # use space in board - ?can we be sure this is complete before function returns?
    self.current = target # updated position
    self.spaces_used = self.spaces_used + 1
    move_list = self.get_moves(self.current)
    self.moves[self.current.tostring()] = move_list #what if current space was encountered earlier?
    
  def backtrack(self):
    """use only when there are no available moves.
    move to previous location and delete top move in move list. Also
    delete last element in self.moves, a point with empty move list
    
    Need to delete used space from board too!
    """  
    
    point = np.fromstring(self.moves.popitem()[0], dtype=int)# pop last item in list, i.e., location where there are no moves
    self.current = np.fromstring(self.moves.keys()[len(self.moves.keys())-1], dtype=int)    # set current to last item
    self.board.free_space(point)
    key = self.current.tostring()
    self.moves[key] = self.moves[key] [1:] #remove first move, already tried
    self.spaces_used = self.spaces_used - 1
    

    
class Knights_tour:
  def __init__(self, start_pos, max, board_size=8):
    self.board = Board(board_size)
    self.knight = Knight(self.board, start_pos)
    self.max_moves = max
    self.total_spaces = self.board.size**2
    
  def run(self):
    i = 1 # first move is placing knight on the board
    while i < self.max_moves:
      print "spaces used: ", self.knight.spaces_used
      if self.knight.spaces_used == self.total_spaces:
        print "Completed tour!"
        break;
        
      self.knight.next_move()
      i = i + 1
    print "used ", i, " moves."
    print "knight covered ", self.knight.spaces_used, " spaces at end."