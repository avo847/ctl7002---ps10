import knights_tour as kt
import numpy as np


#game.knight.print_move_list()

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
        return
      except IndexError:
        print "no solution found when starting at ", p

run()