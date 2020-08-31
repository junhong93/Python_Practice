class Vehicle():
    def __init__(self, vin, make, model):
        self.vin = vin 
        self.make = make
        self.model = model
        self.running = False
        print(f"Vehicle created {vin, make, model}")
    
    def start(self):
        print("Car started...")
        self.running = True
        

    def stop(self):
        print("Car stopped...")
        self.running = False
    

car = Vehicle("TS123", "Tesla", "Model S")
car.start()
plane = Vehicle('X99Y', "Boeing", "747-B")
plane.stop()



class FastVehicle(Vehicle):
    def stop(self):
        print("I can't stop")
        self.running = True

car = FastVehicle("T124", "Tesla", "Model X")
car.start()
car.stop()