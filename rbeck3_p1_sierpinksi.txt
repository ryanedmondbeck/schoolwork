# Ryan Beck | MCS 275 | Project 1 | 10.2.18

import matplotlib.pyplot as plt
import random

# dice generates number from 1 - 6
class Dice(object):

	def roll(self):
		r = random.choice([1,2,3,4,5,6])
		return r

class Sierpinski(Dice):
	X = [] # holds all x coordinates
	Y = [] # holds all y coordinates

	def __init__(self, vertex_points, number_of_iterations, current_pos_x, current_pos_y):
		self.vp = vertex_points
		self.num_it = number_of_iterations
		self.cx = current_pos_x
		self.cy = current_pos_y
		Dice.__init__(self)

	# randomly generates points based on size of input
	def generate_data(self):
		self.X.append(self.cx)
		self.Y.append(self.cy)
		for i in range(0, self.num_it):
			r = self.roll()
			if r == 1 or r == 2:
				self.cx = (self.cx + self.vp[0][0]) / 2
				self.X.append(self.cx)
				self.cy = (self.cy + self.vp[0][1]) / 2
				self.Y.append(self.cy)
			if r == 3 or r == 4:
				self.cx = (self.cx + self.vp[1][0]) / 2
				self.X.append(self.cx)
				self.cy = (self.cy + self.vp[1][1]) / 2
				self.Y.append(self.cy)
			if r == 5 or r == 6:
				self.cx = (self.cx + self.vp[2][0]) / 2
				self.X.append(self.cx)
				self.cy = (self.cy + self.vp[2][1]) / 2
				self.Y.append(self.cy)

	def plot_data(self):
		plt.plot(self.X, self.Y, 'r-')
		plt.grid()
		plt.show()

def main():
	#S = Sierpinski([[P1x,P1y],[P2x,P2y],[P3x,P3y]], number_of_iterations, current_pos_x, current_pos_y)
	S = Sierpinski([[0,0],[20,20],[40,0]], 10000, 1, 1)
	S.generate_data()
	S.plot_data()

main()