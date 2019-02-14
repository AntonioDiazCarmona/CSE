class Faucet(object):
    def __init__(self,pull_handles,water_per_minute,amount_water,hot,cold):
        #these are things that a WaterGun has.
        # all of these should be relevant to our program.
        self.cold          # hot and cold is a methiod
        self.hot
        self.pressure               # method
        self.amount_water
        self.water_per_minute =
        self.pull_handles
    def pull_handles(self, time):
        if self.handles:
            if self.pressure <= 0:
                print("There's no pressure!")
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
        print("You pump the tank back to full pressure")

# Initialize the objects
Faucet.