class student:
    def __init__(self,name,rollno,section):
        self.name = name
        self.rollno = rollno
        self.section = section

    def show(self):
        print(self.name,self.rollno,self.section)

    class section:
        def __init__(self):
            self.total = "100"
            self.male = "25"
            self.female = "75"

        def show(self):
            print(self.total,self.male,self.female)

s1 = student("kavin",2,"A")
s2 = student("Bhuvi",1,"A")
s1.show()
s2.show()
s1.show()