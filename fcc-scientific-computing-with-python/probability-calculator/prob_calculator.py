import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **args):
		self.contents = []
		for x in args:
			for i in range(args[x]):
				self.contents.append(x)
		self.contents_start = self.contents
	
	def draw(self, n):
		drawn = []
		if n <= len(self.contents):
			for x in range(n):
				i = random.choice(self.contents)
				drawn.append(i)
				self.contents.remove(i)
		else:
			drawn = self.contents
		return drawn


		

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	correct = 0
	for x in range(num_experiments): #experiment instance
		success = False
		b = copy.copy(expected_balls)
		d = hat.draw(num_balls_drawn)

		for i in b.keys():
			d_c = d.count(i)
			if d_c >= b[i]:
				success = True
			else:
				success = False
				break
		
		if success:
			correct += 1
		hat.contents = copy.copy(hat.contents_start)
	
	probability = correct/num_experiments
	return probability
