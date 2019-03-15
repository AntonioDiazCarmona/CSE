class Hoverboard():
    def __init__(self, turn_on='False', top_speed=25, forward_speed=10, backwards_speed=5, right_speed=5, left_speed=5,
                 color='white'):
        # these are the things that hoverboard has
        self.forward = forward_speed
        self.backwards = backwards_speed
        self.right_speed = right_speed
        self.left_speed = left_speed
        self.top_speed = top_speed
        self.color = color
        self.turn_on = turn_on
        self._turn_on()

    def _turn_on(self):
        if self.turn_on == True:
            print("Welcome to your new hoverboard!")
        #  if its is true in init basically means it wont ask you you else which is would you like to turn on hoverboard
        else:
            ans = input('Would you like to turn the hoverboard on?')  # it asks this because for init its put to false
            if ans.lower() == 'yes':
                self.turn_on = True
                self._turn_on()
            else:
                print('Okay, goodbye.')

    def go_forward(self):

        if self.turn_on == True:
            print('Moving forward!')
        else:
            print('Is the hoverboard on?')

    def go_backwards(self):
        if self.turn_on:
            print("Going backwards")
        else:
            print('is the hoverboard even on?')

    def go_right(self):
        if self.turn_on:
            print("you are going to the right")
        else:
            print("is the hoverboard even on?")

    def go_left(self):
        if self.turn_on:
            print("you are going to the left")
        else:
            print("Is the hoverboard even on?")


h1 = Hoverboard('False', 10, 6, 5, 2, 3, 'Black')
h1.go_forward()
h1.go_right()
