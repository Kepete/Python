class FirstSingleton(object):

	_instance = None
	def __new__(self):
		if not self._instance: #Check if value in instance
			self._instance = super(FirstSingleton, self).__new__(self) #if not create it 
			self.a = 50
		return self._instance # and return it

b = FirstSingleton()
print (b.a)
b.a = 100

c = FirstSingleton()
print (c.a)
	