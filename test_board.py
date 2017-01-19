import knights_tour as kt
import numpy as np
    
    
#Test class board
print "ok"
my_board = kt.Board()
print "made board"
p = np.array([1,2])
if my_board.is_free(p):
  print "the point ", p , " is free"
else: 
  print "the point ", p ," is not free"
  
my_board.use_space(p)
print "used space (1,2) "

print "spaces used: ", my_board.spaces_used
if my_board.is_free(p):
  print "the point ", p , " is free"
else: 
  print "the point ", p , " is not free"
  

my_board.use_space(p)
print "spaces used: ", my_board.spaces_used