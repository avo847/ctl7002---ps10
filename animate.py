import knights_tour as kt
from matplotlib import pyplot as plt
from matplotlib import animation
import collections as coll
import numpy as np
import pdb

# fist set up the figure, the axizm and plot the element 
# we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0,8), ylim=(0,8))
line, = ax.plot([], [], lw=2, marker='o')
plt.grid()

def init():
  line.set_data([], [])
  return line,

# the game
p = np.array([0,0])
game=kt.Knights_tour(p,50000)
print "starting tour at ", p
if game.knight.spaces_used == 64:
  print "Solution found when starting at ", p
  print "spaces used: ", game.board.spaces_used
          
  
# animatiob function. This is called sequantially
def animate(i):
  game.knight.next_move()
  x = 0.5 + game.board.spaces_used[:,1]
  y = 7.5- game.board.spaces_used[:,0]
  line.set_data(x,y)
  return line,
  
# call the animator
# blit = True means only redraw parts that have changed
anim = animation.FuncAnimation(fig, animate, init_func=init,
                                               frames=200, interval=50, blit=True)

plt.show()                                          