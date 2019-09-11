class T1:
    def __init__(self, p2):
        self.p1 = 1
        self.p2 = p2

class T2(T1):
    def __init__(self, p3):
        super().__init__(2)
        self.p3 = p3

t1 = T1(2)
t2 = T2(3)

print(t2.p1)
print(t2.p2)
print(t2.p3)