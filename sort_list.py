



class A:
    def play(self):
        print("this is main function")
	
class B(A):
   def sing(self):
        print(" this is derived function")
   
d=B()
d.sing()
d.play()