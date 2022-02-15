class Rectangle:
	def __init__(self, w, h):
		self.type = "Rectangle"
		self.width = w
		self.height = h
	
	def __str__(self):
		str_r = "Rectangle(" + "width=" + str(self.width) + ", height=" + str(self.height) + ")"
		return str_r
	
	def set_width(self, w):
		self.width = w
	
	def set_height(self, h):
		self.height = h
	
	def get_area(self):
		area = self.width * self.height
		return area
	
	def get_perimeter(self):
		perimeter = (2*self.width) + (2*self.height)
		return perimeter
	
	def get_diagonal(self):
		diagonal = (self.width ** 2 + self.height ** 2) ** .5
		return diagonal

	def get_picture(self):
		shape_r = ""
		if self.width > 50 or self.height >50:
			shape_r = "Too big for picture."
		else:
			for x in range(self.height-1):
				shape_r += "*" * self.width + "\n"
			shape_r += "*" * self.width + "\n"
		
		return shape_r
	
	def get_amount_inside(self, shape):
		all_fit = int(self.get_area()/shape.get_area())
		if all_fit < 0:
			all_fit = 0
		return all_fit


class Square(Rectangle):
	def __init__(self, side):
		Rectangle.__init__(self, side, side)
	
	def __str__(self):
		str_r = "Square(" + "side=" + str(self.width) + ")"
		return str_r

	def set_side(self, s):
		self.width = s
		self.height = s
	
	def set_width(self, w):
		self.width = w
		self.height = w
	
	def set_height(self, h):
		self.height = h
		self.width = h
