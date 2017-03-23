import knights_tour as kt
from matplotlib import pyplot as plt
from matplotlib import animation
import collections as coll
import numpy as np
import matplotlib

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, bitrate=1000, metadata=dict(title="Knight's Tour Animation", artist='Albert Reidak Pena'))

# fist set up the figure, the axis and plot 
# we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0,8), ylim=(0,8)) # for 8x8 grid
line, = ax.plot([], [], lw=2, marker='o')
ax = plt.title("ctl7002 - Knight's Tour, using Warnsdorf's heuristic")
plt.grid()

def init():
  line.set_data([], [])
  return line,

# the game
p = np.array([3,3])   # starting point
max_steps = 50000
board_size=8
game=kt.Knights_tour(p,max_steps, board_size)  #create game object
          
  
# animatiob function. This is called sequantially
def animate(i):
  if game.knight.spaces_used == board_size**2:
    return line,
  game.knight.next_move()
  x = 0.5 + game.board.spaces_used[:,1] # list of x-coord of spaces used in knight's path
  y = 7.5- game.board.spaces_used[:,0] # list of y-coordinates of spaces used in knight's path
  line.set_data(x,y)
  return line,
  
# call the animator
# blit = True means only redraw parts that have changed
anim = animation.FuncAnimation(fig, animate, init_func=init,
                                               frames=800, interval=50, repeat=False, blit=True)

plt.show()                       
                   
#anim.save("Knights Tour animation with Warnsdorfs heuristic.mp4", writer=writer)