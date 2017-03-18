import knights_tour as kt
import numpy as np

p = np.array([0,0])
my_board = kt.Board()
my_knight = kt.Knight(my_board, p)

print "ok"
#print my_knight.get_moves(my_knight.current)
print "move list: "
my_knight.print_move_list()


print "first move:"
my_knight.next_move()
print "ok"
my_knight.print_move_list()


print "spaces used: "
print my_knight.board.spaces_used

print 
print "next move:"
my_knight.next_move()
print "ok"
my_knight.print_move_list()
print "there are ", my_knight.how_many(my_knight.current), " moves"

print "spaces used: "
print my_knight.board.spaces_used
