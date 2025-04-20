import random
import tm1640
from machine import Pin, Timer

###
# Seeed XIAO RP2040 pins relative to RP2040 GPIO
# 
#         Arduino         RP2040 GPIO
#           Pin               Pin
#         ---------------------------
#         A0/D0                26
#         A1/D1                27
#         A2/D2                28
#         A3/D3                29
#         SDA/D4                6
#         SCL/D5                7
#         Tx/D6                 0
#         Rx/Csn/D7             1
#         SCK/D8                2
#         MISO/D9               4
#         MOSI/D10              3
###

##### General helper functions
#List flattener: Digits on LED displays are a list of lists. Convert to just a list.
def flatten_list(list_of_lists):
    return [item for row in list_of_lists for item in row]

#Fisher-Yates shuffle! An efficient randomization technique. Also a form of interpretive dance?
def shuffle(array):
    for i in range(len(array)-1, 0, -1):
        j = random.randrange(i+1)
        array[i], array[j] = array[j], array[i]
        
# Get the index of the tiles that produce a recource, based on a dice roll
def get_indices(lst, targets):
    return [index for index, element in enumerate(lst) if element in targets]

#Interrupt-driven dice roller with debounce. Rolls two dice twice, discards the first roll (probably uneccessary but I though I saw some RNG strangeness without it) 
#If the roll is 7, trigger the "robber"
def ISR_roll(pin):
  roll.irq(trigger=Pin.IRQ_RISING,handler=None)
  random.seed()
  global robber
  global indices
  global current_dice1
  global currentRoll
  current_dice1 =  random.randrange(1,7) 
  current_dice2 =  random.randrange(1,7)
  current_dice1 =  random.randrange(1,7) 
  current_dice2 =  random.randrange(1,7) 
  currentRoll = current_dice1 + current_dice2
  if currentRoll == 7:   
      robber = True
      indices = []
  else:
      indices = []
      robber = False
      currentRoll = num_order[(current_dice1 + current_dice2 - 2)]
      indices = [i for i, x in enumerate(values) if x == currentRoll]
  blinkState = False

# While the roll button is pressed down, blank the board. This is just cosmetic, to provide feedback to user action of pressing the "roll dice" button. 
def ISR_roll_start(pin):
    global current_dice1
    roll.irq(trigger=Pin.IRQ_FALLING,handler=None)
    current_dice1 = 0
    tm0.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    tm1.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    tm2.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    tm3.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    roll.irq(trigger=Pin.IRQ_RISING,handler=ISR_roll)
##### End General helper functions

##### Definitions  
#definitions for terrain. The bits in these integers represent which LEDs are on in the RGB LEDs that represent terrain types on the board.
hill = 2 #red
forest = 4 #green
field = 6 #yellow
mountain = 1 #blue
pasture = 7 #white
dead = 0 #none, for desert and 3:1 ports.

#we also define the numbers to display on the screen, this reflects how the segment displays are wired.
two = [int('01111011', 2),int('00000000', 2)]
three = [int('01111110', 2),int('00000000', 2)]
four = [int('11011100', 2),int('00000000', 2)]
five = [int('10111110', 2),int('00000000', 2)]
six = [int('10111111', 2),int('00000000', 2)]
eight = [int('11111111', 2),int('00000000', 2)]
nine = [int('11111110', 2),int('00000000', 2)]
ten = [int('11110111', 2),int('01000100', 2)]
eleven = [int('01010100', 2),int('01000100', 2)]
twelve = [int('01111011', 2),int('01000100', 2)]
desert = [int('00000000', 2),int('00000000', 2)]

#This list gives the display states the order we expect them to have. Rolls of 7 don't correspond to a tile.
num_order = [two,three,four,five,six,"robber",eight,nine,ten,eleven,twelve]

#The game has two dice, which sum to make the current roll. On startup, we init them to zero so the game knows it hasn't begun yet.
current_dice1 = 0
current_dice2 = 0
currentRoll = 0

#The state of the robber piece -- True means current player can move it. False means they cannot. We init it as False.
robber = False

#We will flash some segments when their value matches the dice roll. Init an empty list for the indices as well as a boolean to handle blinking.
indices = []
blinkState = True

#Choose 'roll dice!' pin.
roll = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)
#roll.irq(trigger=Pin.IRQ_RISING,handler=ISR_roll)
roll.irq(trigger=Pin.IRQ_FALLING,handler=ISR_roll_start)

##### End Definitions



##### Initialize a blank board (so we start from a known state on boot)
tm0 = tm1640.TM1640(clk=Pin(26), dio=Pin(27))
tm0.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
tm0.brightness(1)
tm1 = tm1640.TM1640(clk=Pin(28), dio=Pin(29))
tm1.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
tm1.brightness(1)
tm2 = tm1640.TM1640(clk=Pin(6), dio=Pin(7))
tm2.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
tm2.brightness(1)
tm3 = tm1640.TM1640(clk=Pin(0), dio=Pin(1))
tm3.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
tm3.brightness(1)
##### End blank board initilazation

##### Functions to initialize, assemble, and display the game data.

# Assemble game state into a list of bytes for the tm1640 to display
def assemble(segment_values,segment_terrain,segment_ports):
    # List of 16 bytes
    segment = segment_values # All 12 numerical display values
    segment_terrain.reverse() # LED positions are addressed backward relative to the numeric displays. I forget why. Probably the way I wired it.
    i = 0
    # Add Terrain RGB LED values
    while i<6:
        segment.append(segment_terrain[i] + 8*segment_terrain[i+1])
        i = i+2
        # Ports are a bit weird because we ran low on pins
        # D8 is RG (G16, pin 7,8) and B (G15 pin 8)    
    segment.append(segment_ports[1] + 8*segment_ports[2]) # Add trade ports 1,2
    # Aww no case/switch in micropython
    if segment_ports[0] == mountain:
        segment[14] = segment[14] + 128 # Set bit 8 for trade port 3, blue bit
    elif segment_ports[0] == pasture:
        segment[14] = segment[14] + 128 # Set bit 8 for trade port 3, blue bit
        segment[15] = segment[15] + 64 # Set bit 8 for trade port 3, green bit
        segment[15] = segment[15] + 128 # Set bit 8 for trade port 3, red bit
    elif segment_ports[0] == hill:
        segment[15] = segment[15] + 128 # Set bit 8 for trade port 3, red bit
    elif segment_ports[0] == forest:
        segment[15] = segment[15] + 64 # Set bit 7 for trade port 3, green bit
    elif segment_ports[0] == field:
        segment[15] = segment[15] + 64 # Set bit 8 for trade port 3, green bit
        segment[15] = segment[15] + 128 # Set bit 7 for trade port 3, red bit      
    elif segment_ports[0] == dead:
        pass
    return segment

# Take the lists that represent the game state, and assemble each into a list of bytes for each segment (4 total)
def init (values,terrain,ports):
    # Slice out the values for each segment
    segment1_values = flatten_list(values[:6])
    segment1_terrain = terrain[:6]
    segment1_ports = ports[:3]

    segment2_values = flatten_list(values[6:12])        
    segment2_terrain = terrain[6:12]
    segment2_ports = ports[3:6]

    segment3_values = flatten_list(values[12:18])
    segment3_terrain = terrain[12:18]
    segment3_ports = ports[-3:]

    # Center 'segment', just one tile
    segment4_values = flatten_list(values[-1:])
    segment4_terrain = terrain[-1:]
    # No ports in center tile

    # Assemble up 3 main segments, then the center tile
    segment1 = assemble(segment1_values,segment1_terrain,segment1_ports)
    segment2 = assemble(segment2_values,segment2_terrain,segment2_ports)
    segment3 = assemble(segment3_values,segment3_terrain,segment3_ports)
    segment4 = segment4_values
    segment4.append(segment4_terrain[0])
    return segment1,segment2,segment3,segment4


##### Function to display whatever you pass it on the board.         
def display(seg1, seg2, seg3,seg4):
    # first 12 grid positions on each segment are the 7-seg displays -- slice 6 from the array for each segment
    tm0.write(seg1)
    tm1.write(seg2)
    tm2.write(seg3)
    tm3.write(seg4)

##### End game data functions

##### Set up the game
# Randomize and set up the board -- define the terrain, numeric values, and ports. Then shuffle them around randomly. Also define a blank board state for convenience later.
terrain = [hill,hill,hill,field,field,field,field,pasture,pasture,pasture,pasture,mountain,mountain,mountain,forest,forest,forest,forest]
values = [two,three,three,four,four,five,five,six,six,eight,eight,nine,nine,ten,ten,eleven,eleven,twelve,desert]
ports = [dead,dead,dead,dead,hill,field,pasture,mountain,forest]
zeroValues = [desert]*20 # Blank board state.
# Randomize values and terrain
shuffle(terrain)
shuffle(values)
# Randomize trade ports
shuffle(ports)

# Insert the desert dead tile at the same index as the actual desert, but in the terrain list
desertIndex= values.index(desert)
terrain.insert(desertIndex, dead)
   
# Driver to assemble and display the game for the first time.
segment1, segment2, segment3, segment4 = init(values,terrain,ports)
display(segment1, segment2, segment3, segment4)


#Now, the main game loop
def main(x):
    global blinkState
    if current_dice1 > 0: #Will always be more than zero if the dice has been rolled at least once, e.g. the game has begun.
        if blinkState == True: # Display the board normally -- blink on whatever was previously off.
            segment1, segment2, segment3, segment4 = init(values,terrain,ports)
            display(segment1, segment2, segment3, segment4)
            roll.irq(trigger=Pin.IRQ_FALLING,handler=ISR_roll_start)
            blinkState = False
        else:
            if currentRoll == 7: # Oh my, a robber!
                segment1, segment2, segment3, segment4 = init(zeroValues,terrain,ports) # Turn off all numeric values on the board, to distract players while they are being robbed.
                display(segment1, segment2, segment3, segment4)
                blinkState = True
            else:
                rollIndex = [i for i, val in enumerate(values) if val == currentRoll]
                tempValues = values.copy()
                for i in rollIndex:
                    tempValues[i]=desert
                segment1, segment2, segment3, segment4 = init(tempValues,terrain,ports) # Turn off just the tiles that produce resources. 
                display(segment1, segment2, segment3, segment4)
                blinkState = True

        
# This handles blink rate
autoroller = Timer(mode=Timer.PERIODIC, period=250, callback=main)

# Do nothing by default. All the needed game logic is triggered by interrupts / timers.
while True:
    pass