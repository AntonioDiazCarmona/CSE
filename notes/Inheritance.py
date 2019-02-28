class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type, body_type):
        super(Car, self). __init__(name, engine_type)
        self.body_type = body_type
        self.steering_wheel = True
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car turns on.")

    def move_forward(self):
        self.fuel -= 1
        print("you move forward.")

    def turn_left(self):
        self.fuel -= 1
        print("you turn left")

    def turn_right(self):
        self.fuel -= 1
        print("you turn right")

    def turn_off(self):
        self.engine_status = False
        print("You turn the engine off.")


class Corvette(Car):
    def __init__(self):
        super(Corvette, self).__init__("Corvette", "Gas", "Slim")


julianna_car = Corvette()
julianna_car.start_engine()
julianna_car.move_forward()
