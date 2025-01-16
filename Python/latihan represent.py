print(repr({"a": 1, "b": 2}))
print(repr([1, 2, 3]))
  
# Custom class
class A():
    def __repr__(self):
        return "\nThis is Area 51\n"
print(repr(A()))

class hewan():
	def anjing():
		print ("gukguk")
	def kucing():
		print ("meong")
	def bebek():
		print("kwek kwek")
	def ayam():
		print ("kukuruyuk")
print(hewan.ayam())