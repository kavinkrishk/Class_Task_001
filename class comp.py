

class bike:

    def spec(self):

        print("100cc,250l,750kg")

kawaski = bike

ktm = bike

print(kawaski)

print(ktm)

bike.spec(kawaski)


kawaski.spec(bike)

ktm.spec(bike)

bike.spec(ktm)