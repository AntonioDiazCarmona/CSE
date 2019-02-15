class Faucet(object):
    def __init__(self, pressure_cold = (1,100),pressure_hot =(1,100),gallons = 50,water_per_minute = 1.5*(1,10)):
        #these are things that a WaterGun has.
        # all of these should be relevant to our program.
        self.percent_cold =  pressure_cold         # hot and cold is a method
        self.percent_hot = pressure_hot
        self.pressure = water_per_minute     # method
        self.amount_water = gallons
        self.pull_handles = True
    def turn_on(self,time):
        if self.pull_handles:
            if self.pressure <= 0:
                print("There's no water coming out!")
            elif self.water_per_minute < time:
               print("You used % water per %s" % self.pressure)
               self.pressure = 0
            else:
                print("You shoot for %s seconds" % time)
                self.pressure -= time
        else:
            print("There is no trigger!")

    def pump_it_up(self):
        self.pressure = 5
        print("water is coming out the faucet at  ")

# Initialize the objects
# Faucet.Pressure