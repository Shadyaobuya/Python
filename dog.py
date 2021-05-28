class Dog():
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
    def sleep(self):
        return "{} Sleep 7 hours a day".format(self.breed)
    def reproduce(self):
        return "My dog, {} gives birth once a year ".format(self.name)

