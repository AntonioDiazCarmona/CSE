from termcolor import colored

debug = True
if debug:
    delay = 0.01
else:
    delay = 1


class LockException(Exception):
    pass


class NeedKeyException(Exception):
    pass


class ToHigh(Exception):
    pass


class Room(object):
    def __init__(self, name, description="", north=None, south=None, east=None, west=None, up=None, down=None,
                 items_in_room=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
        self.west = west
        self.up = up
        self.down = down
        self.items = items_in_room

# ======================================================================================================================


class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Axe(Item):
    def __init__(self, name, weight, blade, damage, durability):
        super(Axe, self).__init__(name, weight)
        self.handle = True
        self.blade = blade
        self.damage = damage
        self.durability = durability

    def blade(self, long):
        self.blade = long

    def damage(self):
        self.damage = 10


class LongAxe(Axe):
    def __init__(self, name, damage, blade, durability, weight):
        super(LongAxe, self).__init__(name, weight, blade, damage, durability)

    def attack(self):
        if self.durability > 0:
            print("you did a heavy swing and did", self.damage, "damage")
            self.durability = self.durability - 5

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long axe")
        else:
            print("you died")


class ShortAxe(Axe):
    def __init__(self, name, damage, blade, durability, weight):
        super(ShortAxe, self).__init__(name, weight, blade, damage, durability)

    def attack(self):
        if self.durability > 0:
            print("you did swing and did", self.damage, "damage")
            self.durability = self.durability - 5

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your short axe")
        else:
            print("you died")


class Sword(Item):
    def __init__(self, name, weight, blade, damage, durability):
        super(Sword, self).__init__(name, weight)
        self.handle = True
        self.blade = blade
        self.damage = damage
        self.durability = durability

    def blade(self, long):
        self.blade = long

    def damage(self):
        self.damage = 10


class ShortSword(Sword):
    def __init__(self, name, damage, blade, durability, weight):
        super(ShortSword, self).__init__(name, weight, blade, damage, durability)

    def attack(self):
        if self.durability > 0:
            print("you did swing your short sword and did", self.damage, "damage")
            self.durability = self.durability - 5

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your short sword")
        else:
            print("you died")


class LongSword(Sword):
    def __init__(self, name, damage, blade, durability, weight):
        super(LongSword, self).__init__(name, weight, blade, damage, durability)

    def attack(self):
        if self.durability > 0:
            print("you did swing your long sword and did", self.damage, "damage")
            self.durability = self.durability - 5

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long sword")
        else:
            print("you died")


class Bow(Item):
    def __init__(self, name, weight, arrows, damage, durability):
        super(Bow, self).__init__(name, weight)
        self.arrows = arrows
        self.damage = damage
        self.durability = durability

    def arrows(self, long):
        self.arrows = long

    def damage(self):
        self.damage = 10


class LongBow(Bow):
    def __init__(self, name, weight, arrows, damage, durability):
        super(LongBow, self).__init__(name, weight, arrows, damage, durability)

    def shoot(self):
        if self.arrows > 0:
            print('swishh swishh I just shot an arrow, you got hit and received', self.damage, 'damage')
            self.arrows = self.arrows - 1
            self.durability = self.durability - 1
        else:
            print('...')

    def how_many_arrows_left(self):
        if self.arrows > 0:
            print("You STILL have", self.arrows, "arrows left")
        else:
            print("You got nothing")
            print(self.arrows)

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long bow")
        else:
            print("you have no durability")


class ShortBow(Bow):
    def __init__(self, name, weight, arrows, damage, durability):
        super(ShortBow, self).__init__(name, weight, arrows, damage, durability)

    def shoot(self):
        if self.arrows > 0:
            print('swishh swishh I just shot an arrow, you got hit and received', self.damage, 'damage')
            self.arrows = self.arrows - 1
            self.durability = self.durability - 1
        else:
            print('...')

    def how_many_arrows_left(self):
        if self.arrows > 0:
            print("You STILL have", self.arrows, "arrows left")
        else:
            print("You got nothing")
            print(self.arrows)

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long bow")
        else:
            print("you have no durability")


class CrossBow(Bow):
    def __init__(self, name, weight, arrows, damage, durability):
        super().__init__(name, weight, arrows, damage, durability)

    def shoot(self):
        if self.arrows > 0:
            print('swishh swishh I just shot an arrow, you got hit and received', self.damage, 'damage')
            less_arrows = int(input("how many arrows would you like to shoot? "))
            self.arrows = self.arrows - less_arrows
            self.durability = self.durability - less_arrows
        else:
            print('...')

    def how_many_arrows_left(self):
        if self.arrows > 0:
            print("You STILL have", self.arrows, "arrows left")
        else:
            print("You got nothing")
            print(self.arrows)

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long bow")
        else:
            print("you have no durability")


class Staff(Item):
    def __init__(self, name, weight, crystal, magic_damage, durability):
        super(Staff, self).__init__(name, weight)
        self.handle = True
        self.crystal = crystal
        self.MagicDamage = magic_damage
        self.durability = durability


class FireStaff(Staff):
    def __init__(self, name, weight, crystal, magic_damage, durability):
        super(FireStaff, self).__init__(name, weight, crystal, magic_damage, durability)

    def shoot_fire_ball(self):
        if self.durability > 0:
            print("you shot a fire ball and did ", self.MagicDamage,
                  "damage, The thing is also taking burn damage of 1 health per sec for 5 secs")
            self.durability = self.durability - 2
            import time
            number_of_seconds = 5
            for _ in range(number_of_seconds):
                time.sleep(1 * delay)
                print("You are taking 1 damage do to fire damage from the fire ball")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your Fire Staff")
        else:
            print("you died")


class IceStaff(Staff):
    def __init__(self, name, weight, crystal, magic_damage, durability):
        super(IceStaff, self).__init__(name, weight, crystal, magic_damage, durability)

    def freeze(self):
        if self.durability > 0:
            print("you shot a Ice ball and ", self.MagicDamage, "damage,You also froze the thing for 10 seconds")
            self.durability = self.durability - 2
            import time
            number_of_seconds = 10
            for _ in range(number_of_seconds):
                time.sleep(1 * delay)
                print("You are frozen ")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your Ice Staff ")
        else:
            print("you died")


class LightingStaff(Staff):
    def __init__(self, name, weight, crystal, magic_damage, durability):
        super(LightingStaff, self).__init__(name, weight, crystal, magic_damage, durability)

    def attack(self):
        if self.durability > 0:
            print("You shot a lighting ball and did ", self.MagicDamage, "damage")
            self.durability = self.durability - 1

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your lighting Staff")
        else:
            print("you died")


class Shield(Item):
    def __init__(self, name, weight, blockdamage, durability):
        super(Shield, self).__init__(name, weight)
        self.blockdamage = blockdamage
        self.durability = durability


class ArmShield(Shield):
    def __init__(self, name, weight, blockdamage, durability):
        super(ArmShield, self).__init__(name, weight, blockdamage, durability)

    def block(self):
        if self.durability > 0:
            damage = int(input("how much damage would you like to recieve? "))
            self.shield_broke(damage)
            self.durability = self.durability - damage
            print("you blocked", damage, "damage")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your arm shield")
        else:
            print("you ran out of durability and your shield broke")

    def shield_broke(self, damage):
        if damage > self.blockdamage:
            print("Your shield broke by taking", self.blockdamage - damage,
                  "damage over the block damage of what the arm shield handle at a time")


class MythicalShield(Shield):
    def __init__(self, name, weight, blockdamage, durability):
        super(MythicalShield, self).__init__(name, weight, blockdamage, durability)

    def block(self):
        if self.durability > 0:
            damage = int(input("how much damage would you like to recieve on your mythical shield? "))
            self.durability = self.durability + damage  # changes
            print("You got attack and you mythical shield absorve", damage,
                  "damage and turned it into durabibility so your durability increase")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you have ", self.durability, "durability after absorbing the damage you took  ")


class NerfGun(Item):
    def __init__(self, name, weight, bullets, damage, durability):
        super(NerfGun, self).__init__(name, weight)
        self.bullets = bullets
        self.damage = damage
        self.durability = durability


class AssaultRifle(NerfGun):
    def __init__(self, name, weight, bullets, damage, durability):
        super(AssaultRifle, self).__init__(name, weight, bullets, damage, durability)

    def shoot(self):
        if self.bullets > 0:
            print('You shot a nerf bullet  with your assault rifle and did ', self.damage, 'damage')
            self.bullets = self.bullets - 1
            self.durability = self.durability - 1
        else:
            print('...')

    def how_many_bullets_left(self):
        if self.bullets > 0:
            print("You STILL have", self.bullets, "bullets left")
        else:
            print("You got nothing")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your nerf assault rifle")
        else:
            print("you have no durability")


class BurstRifle(NerfGun):
    def __init__(self, name, weight, bullets, damage, durability):
        super(BurstRifle, self).__init__(name, weight, bullets, damage, durability)

    def shoot(self):
        if self.bullets > 0:
            print('You shot 3 nerf bullets with your burst rifle and did ', self.damage, 'damage')
            self.bullets = self.bullets - 3
            self.durability = self.durability - 1
        else:
            print('...')

    def how_many_bullets_left(self):
        if self.bullets > 0:
            print("You STILL have", self.bullets, "bullets left")
        else:
            print("You got nothing")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your nerf burst rifle")
        else:
            print("you have no durability")


class ThrowingThings(Item):
    def __init__(self, name, weight, damage):
        super(ThrowingThings, self).__init__(name, weight)
        self.damage = damage


class Rock(ThrowingThings):
    def __init__(self, name, weight, damage):
        super(Rock, self).__init__(name, weight, damage)

    def throw(self):
        if self.damage > 0:
            print("you threw a rock and did", self.damage, "damage")
        else:
            print("You have no muscle and didn't throw the rock.")


class NinjaStar(ThrowingThings):
    def __init__(self, name, weight, damage):
        super(NinjaStar, self).__init__(name, weight, damage)

    def throw(self):
        if self.damage > 0:
            print("you threw a ninja star and did", self.damage, "damage")
        else:
            print("you threw the ninja star but missed...")


class ThingsInGame(Item):
    def __init__(self, name, weight, durability):
        super(ThingsInGame, self).__init__(name, weight)
        self.durability = durability


class Stool(ThingsInGame):
    def __init__(self, name, weight, durability):
        super(Stool, self).__init__(name, weight, durability)

    def place(self):
        if self.durability > 0:
            print("You placed the the stool and you can now reach the top of the statue with no head")
        else:
            print("you need to place the stool closer")


class Flashlight(ThingsInGame):
    def __init__(self, name, weight, durability):
        super(Flashlight, self).__init__(name, weight, durability)


class Keys(ThingsInGame):
    def __init__(self, name, weight, durability):
        super(Keys, self).__init__(name, weight, durability)

    def rotate(self):
        if self.durability > 0:
            print("You rotates the key and opened the door")
        else:
            print("you need to rotate the key to open the mansion door")


# ===========================================Character==================================================================


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Player(object):
    def __init__(self, starting_location, pickup, drop):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10
        self.pickup = pickup                  # you add a pick up method to player because hes the one going pickup
        self.drop = drop

    def move(self, new_location):
        """this method moves characters to a new location

        :param new_location:  the variable containing a room object
        """
        self.current_location = new_location
# ======================================================================================================================


Long_Axe = LongAxe("LongAxe", 30, "Long", 100, 20)
Short_Axe = ShortAxe("ShortAxe", 15, "small", 50, 10)
Short_Sword = ShortSword("ShortSword", 5, "small", 50, 5)
Long_Sword = LongSword("ShortSword", 5, "small", 50, 5)
Long_Bow = LongBow("Long Bow", 15, 10, 50, 500)
Short_Bow = ShortBow("Long Bow", 10, 30, 30, 300)
Cross_Bow = CrossBow("Long Bow", 10, 30, 30, 1000)
Fire_Staff = FireStaff("FireStaff", 20, "Long", 60, 20)
Ice_staff = IceStaff("IceStaff", 20, "Long", 50, 35)
lighting_staff = LightingStaff("lighting staff", 15, "long", 100, 25)
Arm_shield = ArmShield("Arm Shield", 10, 50, 1000)
Mythical_Shield = MythicalShield("Mythical Shield", 10, 0, 500)
Assault_Rifle = AssaultRifle("Assault Rifle", 15, 30, 20, 200)
Burst_Rifle = BurstRifle("Burst Rifle", 15, 20, 15, 100)
rock = Rock("Rock", 4, 10)
Ninja_Star = NinjaStar("Ninja Star", 2, 15)
c1 = Character("Orc1", 100, Long_Axe, None)
c2 = Character("Orc2", 100, Long_Bow, None)
stool = Stool("stool", 10, 100)
key = Keys("key", 1, 1000)
SecondKey = Keys("SecondKey", 1, 1000)
flashlight = Flashlight("FlashLight", 1, 50)
# ================================================Rooms=================================================================
MANSION_DOOR = Room("The Abandoned Mansion Door", "The door seems to be closed and around you can see plants.\n"
                                                  "To the south there is a window. To the west is a statue that\n"
                                                  "has no head. ")
MANSION_WINDOW = Room("East Side Window", "The window seems to be a mirror. ")

EAST_SIDE_OF_MANSION = Room("East Side Of Mansion", "The east side of the mansion seems to be blocked off by a giant\n"
                                                    "tree. There is also a short sword leaning on the tree\n"
                                                    "it looks very very old.", None, None, None,
                            None, None, None, Short_Sword)
V2MANSION_WINDOW = Room(" East Side Window of Mansion", "You are back to the window that seems to be a mirror.")

STATUE = Room("Cobblestone statue", "What your looking at is a cobble stone statue of a man with no head.\n"
                                    "You can see a metal piece on top of the statue where there is no head\n"
                                    "the statue is to high you will need something to climb on the statue and\n"
                                    "get the metal piece.To the south is the west side of the mansion.", None, None,
              None, None, None, None, key)

V1_SIDE_OF_MANSION = Room("West side of mansion", "You are looking down the south side of mansion which leads"
                                                  " to the backyard.")

DOWN_SIDE_OF_MANSION = Room("Down south side of mansion", "You walked down the south side of mansion,"
                                                          " to the east is the backyard of mansion\n")

BACKYARD_OF_MANSION = Room("East Backyard", "You are at the back yard and their seems to be a lot of items at\n"
                                            "the backyard like a slide a stool and a lot of tables for some reason.",
                           None, None, None, None, None, None, stool)

V2_SIDE_OF_MANSION = Room("West Side of Mansion", "You are looking at the side of the mansion you came from\n"
                                                  "to go back up go to the north")

UP_SIDE_OF_MANSION = Room("Up North, West Side Of Mansion ", "You walked up the north side of mansion which was the way"
                                                             "\n"
                                                             "you walked in the beginning to go to the back yard.\n"
                                                             "To the east is the west side of mansion.")

V3_SIDE_OF_MANSION = Room("West side of mansion", "You are at the west side of mansion to the east is\n"
                                                  "the cobblestone statue from before.")

COBBLE_STONE_STATUE = Room("WEST COBBLE STONE STATUE", "You are back at the cobblestone statue now try to see what\n"
                                                       "is the top of the statue, since you picked up the stool\n"
                                                       "and you have it in your inventory you dont need to\n"
                                                       "place it you can just take the thing at the top of\n"
                                                       "the statue\n",
                           None, None, None, None, None, None, key)
# you find the key...

V2MANSION_DOOR = Room("FRONT MANSION DOOR", "You are back again to front mansion now try to open with\n"
                                            "the key you got from the top of the cobbles stone\n"
                                            "statue with not head, by going south.")  # you get the key

INSIDE_MANSION = Room("INSIDE OF MANSION", "Their seems to be a lot of rooms inside the mansion.\n"
                      "The first floor of the mansion has two rooms one to the the west and one to the east. to the\n"
                      "south their are two stair leading up to the second floor which where you\n"
                      "can see more rooms. Their is also a random doll sitting on one of\n"
                                           "the stairs.")

First_floor_of_mansion_west = Room("West room first floor", "You are at the west room of the first floor\n"
                                                            "to try to open the door of the room go west\n")

First_floor_of_mansion_west_locked = Room("The door is locked", "You tried opening the door but the door is locked.\n"
                                                                "And I don't think you can open it because it has a\n"
                                                                "handle on the door but no key mold to open it.\n"
                                                                "Which means the door\n"
                                                                "was locked from the inside.")

First_floor_of_mansion_east = Room("East room first floor", " You are at the east room try to open the room by going"
                                                            " east")

First_floor_of_mansion_east_blocked = Room("The door is blocked", "The door wasn't locked and you opened it however\n"
                                                                  "when you opened the door behind it was a concrete\n"
                                                                  "wall blocking the entrance to the inside of the\n"
                                                                  "room.So basically you cant go in unless you get a\n"
                                                                  "hammer which who would keep a  sledge hammer in a\n"
                                                                  "mansion")

Stairs = Room("Stairs", "You are at the stairs.To go up the stairs you would need to go south")

Up_stairs = Room("Up stairs", "You are going up the stairs soon you are going to choose\n"
                              "which stairs you want to go on\n"
                              "the one with the doll that looks like the stairs are\n"
                              "brand new which is to the east\n"
                              "or the one that looks very old\n"
                              "and looks likes its going to break as soon at you step on one which is to the west.")


west_stairs = Room("west stairs", "That's kind of weird why would you pick the stairs\n"
                                  "that look likes they are going\n"
                                  "to break I guess just go south if you want to go up the stairs.")

up_west_stairs = Room("Up west stairs", "You are going up the west stairs keep going up by going south ")

fell_off_the_west_stairs = Room("Fell off", "Boom you fell off I warned you don't go on these stairs but you went\n "
                                "anyway and now you are stuck because you seem to be inside the stairs and\n"
                                "you cant get out.However in the bright side you found\n"
                                "a secret room. Their seems to be a lot of things here maybe you can find something\n"
                                "that can help you get out or even lead some where else\n")

North_inside_west_stairs = Room("north", "To the north you see nothing.")

West_inside_west_stairs = Room("west", "To the west you can see a  shield  you might want to pick it you might need\n"
                                       "it for something", None, None, None, None, None, None, Arm_shield)

East_inside_west_stairs = Room("east", "To the east you don't really see nothing besides a giant picture frame on the\n"
                                       "wall.")

South_inside_west_stairs = Room("south", "To the south their is a random book with the title being help you might\n"
                                         "probably want to read it, maybe it can give you a clue of how to get out\n"
                                         "to open the book go south.")

Reading_The_Book = Room("Reading Book", "Hello  this is the first day in the mansion I checked all the rooms\n"
                                        "and I found nothing for the longest time since I entered the mansion I felt\n"
                                        "a presence of someone following  me every where or was it my imagination\n"
                                        "The second day I  was trying to go back outside the mansion but the mansion\n"
                        "door was locked and so I decided to  explore  a little more, so I went to the\n"
                        "second floor of the mansion and while I was going their was two path one with\n"
                                        "a random doll on the stairs and the other with very old stairs going up.\n"
                                        "I was going to choose the stairs with the doll but I felt very weird when I\n"
                                        "look at the random doll so I decided to take a risk and go with the very old\n"
                                        "stairs. I went up the stairs but while going up the stairs one of the stairs\n"
                                        "and I fell down the stairs.Now I was inside the stairs and couldn't get out\n"
                                        "even though I tried everything.The third day went by and I was still in the\n"
                                        "mansion and while being stuck in the stairs it made me realize of something\n"
                                        "similar I captured in my dream when I was in a cave and suddenly...The book\n"
                                        "seems to stop right here and on every page after that it says HELP!!!, This\n"
                        "did not give you any information of how to get out however if the person who\n"
                                        "wrote this is, is not here their must be a way to get out of here.\n"
                                        "To close the book go north.")

east_stairs = Room("East stairs", "Wow you pick the stairs with the doll on top of one steps of the stairs.")

up_east_stairs = Room("Up East Stairs", "You went up the east stairs to the east is a room with a broken door\n"
                      "you can see an item in side to the west their is door and it seems to have a key in the door.\n"
                      "To the south its just blocked off by a random piano that looks very clean and looks like\n"
                                        "it has a key mold.\n")

up_stairs_east = Room("upstairs east", "You are outside the east room with the broken door.Their seems to be not much\n"
                                       " inside just a flashlight and footprints in the ground and randomly\n"
                                       " disappear when they got close to the wall to go inside the room go east\n")
#  ADDDDDDDDDDDDDDDDDD a path here
Up_stairs_east_room = Room("Inside upstairs east room", "Your are now inside the east room you see the footprints\n"
                                                        "close and you realize that the closer they get to the wall\n"
                           "the smaller the footprints get like if a grown up  was getting\n"
                                                        "smaller the closer they got to the wall, also you should\n"
                                                        "probably take the flashlight", None, None, None, None, None,
                           None, flashlight)

up_stairs_west = Room("upstairs west", "You are at the door, with the key inside the door.", None, None, None, None,
                      None, None, SecondKey)
up_stairs_south = Room("upstairs south", "You are at the piano with the key mold maybe you have to use a key in\n"
                                         "the piano and something might happen.")

ABANDONED_MANSION = Room("Abandoned Mansion", "What your looking at is an abandoned mansion from\n"
                                              "the gate door a mile away.\n"
                                              "This mansion who no one know's who built it or who live here and some\n"
                         "people have even said that the mansion has been abandoned for centuries\n"
                                              "and it has stayed the same. The mansion has 15 rooms or does it?\n"
                                              "It also has a random statue with no head")

#  you open the door with the key,get in.
# =======================================Instantiate items==============================================================
ABANDONED_MANSION.south = MANSION_DOOR
MANSION_DOOR.north = ABANDONED_MANSION
MANSION_DOOR.east = MANSION_WINDOW
MANSION_DOOR.south = INSIDE_MANSION
MANSION_WINDOW.west = MANSION_DOOR
MANSION_WINDOW.east = EAST_SIDE_OF_MANSION
EAST_SIDE_OF_MANSION.west = V2MANSION_WINDOW
V2MANSION_WINDOW.east = EAST_SIDE_OF_MANSION
V2MANSION_WINDOW.west = MANSION_DOOR
MANSION_DOOR.west = STATUE
STATUE.east = MANSION_DOOR
STATUE.south = V1_SIDE_OF_MANSION
V1_SIDE_OF_MANSION.north = STATUE
V1_SIDE_OF_MANSION.south = DOWN_SIDE_OF_MANSION
DOWN_SIDE_OF_MANSION.north = V1_SIDE_OF_MANSION
DOWN_SIDE_OF_MANSION.east = BACKYARD_OF_MANSION
BACKYARD_OF_MANSION.west = DOWN_SIDE_OF_MANSION
BACKYARD_OF_MANSION.west = V2_SIDE_OF_MANSION
V2_SIDE_OF_MANSION.east = BACKYARD_OF_MANSION
V2_SIDE_OF_MANSION.north = UP_SIDE_OF_MANSION
UP_SIDE_OF_MANSION.south = V2_SIDE_OF_MANSION
UP_SIDE_OF_MANSION.east = V3_SIDE_OF_MANSION
V3_SIDE_OF_MANSION.west = UP_SIDE_OF_MANSION
V3_SIDE_OF_MANSION.east = COBBLE_STONE_STATUE
COBBLE_STONE_STATUE.west = V3_SIDE_OF_MANSION
COBBLE_STONE_STATUE.east = V2MANSION_DOOR
V2MANSION_DOOR.east = MANSION_WINDOW
V2MANSION_DOOR.west = COBBLE_STONE_STATUE
V2MANSION_DOOR.south = INSIDE_MANSION
INSIDE_MANSION.north = V2MANSION_DOOR
INSIDE_MANSION.west = First_floor_of_mansion_west   # first floor rooms
First_floor_of_mansion_west.east = INSIDE_MANSION
First_floor_of_mansion_west.west = First_floor_of_mansion_west_locked
First_floor_of_mansion_west_locked.east = First_floor_of_mansion_west
INSIDE_MANSION.east = First_floor_of_mansion_east
First_floor_of_mansion_east.west = INSIDE_MANSION
First_floor_of_mansion_east.east = First_floor_of_mansion_east_blocked
First_floor_of_mansion_east_blocked.west = First_floor_of_mansion_east
INSIDE_MANSION.south = Stairs   # this is the stairs and going to the second floor
Stairs.north = INSIDE_MANSION
Stairs.south = Up_stairs
Up_stairs.north = Stairs
Up_stairs.west = west_stairs
west_stairs.east = Up_stairs
west_stairs.south = up_west_stairs
up_west_stairs.north = west_stairs
up_west_stairs.south = fell_off_the_west_stairs
fell_off_the_west_stairs.north = North_inside_west_stairs
fell_off_the_west_stairs.east = East_inside_west_stairs
fell_off_the_west_stairs.west = West_inside_west_stairs
fell_off_the_west_stairs.south = South_inside_west_stairs
North_inside_west_stairs.east = East_inside_west_stairs
North_inside_west_stairs.west = West_inside_west_stairs
North_inside_west_stairs.south = South_inside_west_stairs
East_inside_west_stairs.north = North_inside_west_stairs
East_inside_west_stairs.west = West_inside_west_stairs
East_inside_west_stairs.south = South_inside_west_stairs
West_inside_west_stairs.north = North_inside_west_stairs
West_inside_west_stairs.east = East_inside_west_stairs
West_inside_west_stairs.south = South_inside_west_stairs
South_inside_west_stairs.north = North_inside_west_stairs
South_inside_west_stairs.east = East_inside_west_stairs
South_inside_west_stairs.west = West_inside_west_stairs
South_inside_west_stairs.south = Reading_The_Book
Reading_The_Book.north = South_inside_west_stairs
Up_stairs.east = east_stairs
east_stairs.west = Up_stairs
east_stairs.south = up_east_stairs
up_east_stairs.north = east_stairs
up_east_stairs.east = up_stairs_east
up_stairs_east.west = up_east_stairs
up_stairs_east.east = Up_stairs_east_room
Up_stairs_east_room.west = up_stairs_east    # i think im finished with up east room
up_east_stairs.west = up_stairs_west
up_stairs_west.east = up_east_stairs
up_east_stairs.south = up_stairs_south
up_stairs_south.north = up_east_stairs

player = Player(ABANDONED_MANSION, pickup=True, drop=True)
playing = True
directions = ["north", "south", "east", "west", "up", "down"]
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
# ===================================================controller=========================================================
while playing:
    print(colored(player.current_location.name, 'blue'))
    print(colored(player.current_location.description, 'cyan'))
    print()
    if player.current_location.items is not None:
        print(colored("There is a %s here." % player.current_location.items.name, 'magenta'))

        items = player.current_location.items.name
        inventory = []
        print(colored('there is an item, want to pick it up?', 'magenta'))

    command = input(">_")
    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False

    elif command == 'BackPack':
        print("You have these items in your inventory:")
        for item in player.inventory:
            print(item.name)
        print()

    elif player.current_location == STATUE and "take " in command.lower() and Stool not in player.inventory:
        print(colored("The item is to high to take.", 'red'))

    elif player.current_location == COBBLE_STONE_STATUE and "take " in command.lower() and stool not in player.\
            inventory:
        print(colored("the item is to high you should picked up the stool in the back yard.", 'red'))

    elif "take " in command:
        items_name = command[5:]
        if player.current_location.items is not None:
            if player.current_location.items.name == items_name:
                print(colored("you took an item to check what items you have type in BackPack", 'green'))
                player.inventory.append(player.current_location.items)
                player.current_location.items = None
            else:
                print(colored("You don't see one", 'red'))
        else:
            print(colored("There is nothing here", 'red'))

    elif "drop " in command:
        items_name = command[5:]
        item_object = None

        for items in player.inventory:
            if items.name == items_name:
                item_object = items

        if item_object is not None and player.current_location.items is None:
            player.inventory.remove(item_object)
            player.current_location.items = item_object
            print(colored("You dropped an item", 'yellow'))
        elif player.current_location.items is not None:
            print(colored("There is already an item here. You can't drop anything.", 'red'))

    elif command.lower() in directions:
        try:
            # command ='north'#if their is now location you put none# so this basically tell it if i has a path to north
            room_object_that_we_move_to = getattr(player.current_location, command)
            if player.current_location == MANSION_DOOR and command.lower() in ["south", 's']:
                if key not in player.inventory:
                    raise LockException
            if player.current_location == up_stairs_south and command.lower() in ['place key in piano',
                                                                                  'put key in piano']:
                if SecondKey not in player.inventory:
                    raise NeedKeyException

            if room_object_that_we_move_to is None:
                raise AttributeError
            player.move(room_object_that_we_move_to)
        except KeyError:
            print(colored("this key does not exist", 'green'))
        except AttributeError:
            print(colored("I can't go that way.", 'red'))
        except LockException:
            print(colored("It's locked.", 'green'))
        except NeedKeyException:
            print(colored("You need a key to put inside the piano so something happens", 'green'))
    else:
        print(colored("Command Not Recognized", 'red'))
    print()
