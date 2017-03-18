import knights_tour as kt
import numpy as np
import pdb


#game.knight.print_move_list()
"""
def run():
  for i in np.arange(0,8,1):
    for j in np.arange(0,8,1):
      p = np.array([i,j])
      game=kt.Knights_tour(p,500)
      print "starting tour at ", p
      try:
        game.run()
        if game.knight.spaces_used == 64:
          print "Solution found when starting at ", p
          print "spaces used: ", game.board.spaces_used
          #game.knight.print_move_list()
          #print "board says: ", np.shape(game.board.spaces_used), " spaces are used"
          #print game.board.spaces_used
          
          return
      except IndexError:
        print "==== No solution found when starting at ", p, " ===="

run()
"""


p = np.array([0,0])
board_size = 8
n_moves = board_size**2
game=kt.Knights_tour(p,50000000, board_size)
print "starting tour at ", p
game.run()
#pdb.set_trace()
if game.knight.spaces_used == n_moves:
  print "Solution found when starting at ", p
  print "spaces used: ", game.board.spaces_used
          