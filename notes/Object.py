class Faucet(object):
    def __init__(self, pressure_cold=0, pressure_hot =0, gallons = 50,):
        #these are things that a WaterGun has.
        # all of these should be relevant to our program.
        self.percent_cold = pressure_cold         # hot and cold is a method
        self.percent_hot = pressure_hot
        self.water_per_minute = 2    # method
        self.amount_water = gallons
        self.pull_handles = True
    def turn_on(self,time):
        if self.pull_handles:
            if self.water_per_minute <= 0:
                print("There's no water coming out!")     # from here to top is right
            elif self.water_per_minute < time:
                print("You used 2 gallons of water per %s" % self.water_per_minute)
            self.water_per_minute -= time
            print("water comes out for  %s seconds" % time)
            self.water_per_minute = 0
        else:
             print("There is no water!")

    def pull_handles(self):
        self.water_per_minute = 0
        print("Your not pulling the handles so no water is coming out" )

# Initialize the objects
# Faucet.Pressure
My_Faucet = Faucet(2,0,50,)






#Do stuff with the obeject
My_Faucet = turn_on