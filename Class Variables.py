class car:

    wheel = 4

    def __init__(self):
        self.name = "B M W"
        self.price = "25lakhs"
        self.type = "petrol"

c1 = car()
c2 = car()
c2.name = "AUDI"
c1.type = "diesal"
car.wheel = 10 #class name space

if c1.name!=c2.name:
    print("Brands are Different")

else:
    print("Best Brand with Price")

print(c1.name,c1.price,c2.type,c1.wheel)

print(c2.name,c2.price,c1.type,c1.wheel)
