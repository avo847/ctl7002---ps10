import knights_tour as kt
import numpy as np

p = np.array([0,0])
game=kt.Knights_tour(p,10)
game.run()
game.knight.print_move_list()