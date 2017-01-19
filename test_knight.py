import knights_tour as kt
import numpy as np

p = np.array([0,0])
my_board = kt.Board()
my_knight = kt.Knight(my_board, p)

print "ok"
print my_knight.get_moves(my_knight.current)
print "move list: "
my_knight.print_move_list()