class WaterGun(object):
    def __init__(self,capacity,distance,stock):
        #these are things that a WaterGun has.
        # all of these should be relevant to our program.
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.stock = stock
        self.duration_of_pressure = 5

    def shoot(self,time):
        if self.trigger:
            if self.duration_of_pressure <= 0:
                print("There's no pressure!")
            elif self.duration_of_pressure < time:
               print("You ran out of preasure after firing for %s seconds",self.duration_of_pressure)
               self.duration_of_pressure = 0
            else:
                print("You  shoot fpr %s seconds" % time)
                self.duration_of_pressure -= time
        else:
            print("There is no trigger!")

My_water_gun = WaterGun(5.2,40,True)
your_water_gun = WaterGun(1.0,1,False)
wiebe_water_Gun = WaterGun(999999999,999999999999,True)