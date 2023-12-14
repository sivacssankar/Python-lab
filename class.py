class rec:
    def __init__(self):
        self.l=int(input("enter length"))
        self.b=int(input("enter breadth"))
    def are(self):
        return self.l*self.b
    def per(self):
        return 2*self.l*self.b
    def com(self,other):
        if self.are()==other.are():
            print("both area are same")
        else:
            print("not same")
rect1=rec()
print("enter 2nd rectangle length and breadth:")
rect2=rec()
print("area:",rect1.are())
print("perimeter:",rect1.per())

print("area of 2nd rect:",rect2.are())
print("perimeter of 2nd rect:",rect2.per())
print(rect1.com(rect2))
