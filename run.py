import knights_tour as kt
import numpy as np
from matplotlib import pyplot as plt


p = np.array([0,0]) #starting point
max_steps=50000
board_size = 8

game=kt.Knights_tour(p,max_steps, board_size) #create game object

print "starting tour at ", p
game.run()

if game.knight.spaces_used == board_size**2:
  print "Solution found when starting at ", p
  print "spaces used: ", game.board.spaces_used
  
  # set up plot for result
  fig = plt.figure()
  ax = plt.axes(xlim=(0,8), ylim=(0,8)) # for 8x8 grid
  line, = ax.plot([], [], lw=2, marker='o')
  ax = plt.title("ctl7002 - Knight's Tour")
  plt.grid()
  # plot data
  x = 0.5 + game.board.spaces_used[:,1] # list of x-coord of spaces used in knight's path
  y = 7.5- game.board.spaces_used[:,0] # list of y-coordinates of spaces used in knight's path
  line.set_data(x,y)
  # display graph
  plt.show()
  
  