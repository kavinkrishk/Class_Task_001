
class computer:

    def __init__(self,name,cpu,ram):
        self.name = name
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("your laptop is",self.name,"& config is",self.cpu,self.ram)

comp1 = computer("HP","i5","8GB")

comp2 = computer("APPLE","i3","4GB")

comp1.config()


comp2.config()

computer.config(comp1)

computer.config(comp2)