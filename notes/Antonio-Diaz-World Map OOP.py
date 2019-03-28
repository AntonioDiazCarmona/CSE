debug = True
if debug:
    delay = 0.01
else:
    delay = 1


class LockException(Exception):
    pass


class Room(object):
    def __init__(self, name, description="", north=None, south=None, east=None, west=None, up=None, down=None,
                 items=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
        self.west = west
        self.up = up
        self.down = down
        self.items = items

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
    def __init__(self, starting_location, pickup):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10
        self.pickup = pickup                  # you add a pick up method to player because hes the one going pickup

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
key = Keys("Key", 1, 1000)

# ================================================Rooms=================================================================
MANSION_DOOR = Room("The ABANDONED MANSION DOOR", "The door seems to be closed and around you can see plants."
                                                  " To the south there is a window. To the west is a statue that"
                                                  " has no head.The door seems to be closed and around you can see"
                                                  " plants.")
MANSION_WINDOW = Room("EAST SIDE WINDOW", "The window seems to be a mirror ")

EAST_SIDE_OF_MANSION = Room("EAST SIDE OF MANSION", "The east side of the mansion seems to be blocked off by a giant"
                                                    " tree. There is also a short sword leaning on the tree"
                                                    " it look very very old.", None, None, None,
                            None, None, None, Short_Sword)
V2MANSION_WINDOW = Room("EAST SIDE WINDOW OF MANSION", "You are back to the window that seems to be a mirror")

STATUE = Room("Cobblestone statue", "What your looking at is a cobble stone statue of a man with no head "
                                    "You can see a metal piece on top of the statue with there is no head"
                                    "the statue is to high you will need something to climb on the statue and"
                                    "get the metal piece,to the south is the west side of the mansion.", None, None,
              None, None, None, None, key)

V1_SIDE_OF_MANSION = Room("West side of mansion", "You are looking down the south side of mansion which leads"
                                                  " to the backyard.")

DOWN_SIDE_OF_MANSION = Room("Down south side of mansion", "You walked down the south side of mansion, to the "
                                                          "east is the backyard of mansion")

BACKYARD_OF_MANSION = Room("EAST BACKYARD", "You are at the back yard and their seems to be a lot of items at"
                                            " the backyard like a slide a stool and a lot of tables for some reason.",
                           None, None, None, None, None, None, stool)

V2_SIDE_OF_MANSION = Room("WEST SIDE OF MANSION", "You are looking at the side of the mansion you came from, to go"
                                                  " back up go to the north")

UP_SIDE_OF_MANSION = Room("UP NORTH,WEST SIDE OF MANSION", "You walked up the north side of mansion which was the way"
                                                           " walked in the begining to go to the back yard, to the east"
                                                           " is the west side of mansion")

V3_SIDE_OF_MANSION = Room("West side of mansion", "You are at the west side of mansion to the east is"
                                                  " the cobblestone statue from before")

COBBLE_STONE_STATUE = Room("WEST COBBLE STONE STATUE", "You are at the cobblestone statue now try to see what"
                                                       " is the top of the cobblestone statue with no head"
                                                       " by placing the stool that you collected from the"
                                                       " backyard and try climbing it to see what was"
                                                       " at the top of the no head statue")
# you find the key...

V2MANSION_DOOR = Room("FRONT MANSION DOOR", "Your are back again to front mansion now try to open with"
                                            " the key you got from the "             
                                            "top of the cobbles stone statue with not head")  # you get the key

INSIDE_MANSION = Room("INSIDE OF MANSION", "Their seems to be a lot of rooms here.Their are two stair leading up to "
                                           "the second floor which where you can see more rooms.Their is also a"
                                           " random doll sitting on the stairs")

ABANDONED_MANSION = Room("Abandoned Mansion", "What your looking at is an abandoned mansion from"
                                              " the gate door a mile away."
                                              " This mansion who no one know's who built it or who live here and some"
                                              " people have even said that the mansion has been abandoned for centuries"
                                              " and it has stayed the same. THe mansion has 15 rooms or does it?"
                                              " It also has a random statue with no head")

#  you open the door with the key,get in.
# =======================================Instantiate items==============================================================
ABANDONED_MANSION.south = MANSION_DOOR
MANSION_DOOR.north = ABANDONED_MANSION
MANSION_DOOR.east = MANSION_WINDOW
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
V2MANSION_DOOR.west = COBBLE_STONE_STATUE
V2MANSION_DOOR.south = INSIDE_MANSION
INSIDE_MANSION.north = V2MANSION_DOOR

player = Player(ABANDONED_MANSION, pickup=True)
playing = True
directions = ["north", "south", "east", "west", "up", "down"]

# ===================================================controller=========================================================
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    print()   # trying to add the pick up method
    # print(player.inventory + player.pickup.items)

    if player.current_location.items is not None:
        print("There is a %s here." % player.current_location.items.name)


    # if player.pickup.items.name == True:
    #       print("do you want to pick up item")
    # if int(input("yes")):
    #       print"you now pick up the", Items

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            # command ='north'#if their is now location you put none# so this basically tell it if i has a path to north
            room_object_that_we_move_to = getattr(player.current_location, command)
            if player.current_location == MANSION_DOOR and command.lower() in ["south", 's']:
                if key not in player.inventory:
                    raise LockException

            if room_object_that_we_move_to is None:
                raise AttributeError
            player.move(room_object_that_we_move_to)
        except KeyError:
            print("this key does not exist")
        except AttributeError:
            print("I can't go that way.")
        except LockException:
            print("It's locked.")
    else:
        print("Command Not Recognized")
    print()
