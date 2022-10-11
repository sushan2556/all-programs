class Father:
    def _init_(self):
	    print("Father Class Constructor")
    def showF(self):
        print("Father Class Method")

class Mother:
	def _init_(self):
		print("Mother Class Constructor")
	def showM(self):
		print("Mother Class Method")

class Son(Father,Mother):
    def _init_(self):
        super()._init_()
    def showS(self):
        print("Son Class Method")

s = Son()
s.showF()
s.showM()
s.showS()