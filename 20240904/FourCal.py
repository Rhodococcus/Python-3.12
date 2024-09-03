class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
    
a = FourCal(4, 2)
b = FourCal(1, 7)

a.setdata(4, 2)
b.setdata(3, 8)

a.add()
b.add()
print(a.add())
print(b.add())

a.mul()
b.mul()
print(a.mul())
print(b.mul())

a.sub()
b.sub()
print(a.sub())
print(b.sub())

a.div()
b.div()
print(a.div())
print(b.div())

