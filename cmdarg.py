class Cmd:
	def __init__(self,message):
		self.message = message[1:]
		self.args = {}

		for i in range(len(self.message)):
			each = self.message[i]
			if each[0] == "-":
				# key
				try:
					self.args[each] = self.message[ i+1 ]
				except (IndexError):
					self.args[each] = None
	
	def get_value(self,key,default = None):

		if self.args[key] == None:
			self.args[key] = default
		return self.args[key]
