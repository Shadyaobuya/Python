class Car():
    def __init__(self,model,registration_number,color,speed):
        self.model=model
        self.registration=registration_number
        self.color=color
        self.speed=speed
    def move(self):
        return "{} move at a speed of {} km/hr ".format(self.model,self.speed)
    def get_details(self):
        return "Model: {}, Registration Number:{}, Color:{}, Speed:{} ".format(self.model,self.registration,self.color,self.speed)

