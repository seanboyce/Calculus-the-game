import random
import tm1640
from machine import Pin, Timer

#functions
def flatten_list(list_of_lists):
    return [item for row in list_of_lists for item in row]

def shuffle(array):
    #classic in-place shuffle
    for i in range(len(array)-1, 0, -1):
        j = random.randrange(i+1)
        array[i], array[j] = array[j], array[i]
        
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
  print(currentRoll)
  if currentRoll == 7:   
      robber = True
      indices = []
  else:
      indices = []
      robber = False
      currentRoll = num_order[(current_dice1 + current_dice2 - 2)]
      indices = [i for i, x in enumerate(values) if x == currentRoll]
  blinkState = False
  
def ISR_roll_start(pin):
    global current_dice1
    roll.irq(trigger=Pin.IRQ_FALLING,handler=None)
    current_dice1 = 0
    tm0.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    tm1.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    tm2.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    roll.irq(trigger=Pin.IRQ_RISING,handler=ISR_roll)
    
#definitions
hill = 2 #red
forest = 4 #green
field = 6 #yellow
mountain = 1 #blue
pasture = 7 #white


#The game has two dice, which sum to make the current roll
current_dice1 = 0
current_dice2 = 0
currentRoll = 0

#The state of the robber piece -- True means current player can move it. False means they cannot.
robber = False

#We will flash some segments when their value matches the dice roll
indices = []
blinkState = True

#we also define the numbers to display on the screen, because I don't remember how I wired the segment displays

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

#This is the numeric order of the display values above.
num_order = [two,three,four,five,six,"robber",eight,nine,ten,eleven,twelve]


#board setup on boot
terrain = [hill,hill,hill,field,field,field,field,pasture,pasture,pasture,pasture,mountain,mountain,mountain,forest,forest,forest,forest]
values = [two,three,three,four,four,five,five,six,six,eight,eight,nine,nine,ten,ten,eleven,eleven,twelve]
shuffle(terrain)
shuffle(values)
print(terrain)

#Blank the board
tm0 = tm1640.TM1640(clk=Pin(0), dio=Pin(1))
tm0.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
tm0.brightness(1)
tm1 = tm1640.TM1640(clk=Pin(2), dio=Pin(3))
tm1.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
tm1.brightness(1)
tm2 = tm1640.TM1640(clk=Pin(4), dio=Pin(5))
tm2.write([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
tm2.brightness(1)

def display(terrain, values):
    # first 12 grid positions on each segment are the 7-seg displays -- slice 6 from the array for each segment
    segment1_values = flatten_list(values[:6])
    segment2_values = flatten_list(values[6:12])
    segment3_values = flatten_list(values[-6:])

    # Terrain types are a bit harder. In a given byte, first 3 bits are RGB for the first LED, second 3 bits are RGB for the next LED, and last two are unused. So we take the value for the first LED, multiply by 2^3, then add the value for the second LED. Then last two bits are blank, so multiply all by 4 -- so x32 and x4
    segment1_terrain = [terrain[0]*8 + terrain[1], terrain[2]*8+terrain[3],terrain[4]*8+terrain[5]]
    segment2_terrain = [terrain[6]*8 + terrain[7], terrain[8]*8+terrain[9],terrain[10]*8+terrain[11]]
    segment3_terrain = [terrain[12]*8 + terrain[13], terrain[14]*8+terrain[15],terrain[16]*8+terrain[17]]

    #Final array for section 1 of board
    allseg1 = segment1_values
    allseg1.extend(segment1_terrain)
    allseg1.append(0) # Grid 16 not connected

    #Final array for section 2 of board
    allseg2 = segment2_values
    allseg2.extend(segment2_terrain)
    allseg2.append(0) # Grid 16 not connected

    #Final array for section 3 of board
    allseg3 = segment3_values
    allseg3.extend(segment3_terrain)
    allseg3.append(0) # Grid 16 not connected

    #Out we go!
    tm0.write(allseg1)
    #print(allseg1)
    tm1.write(allseg2)
    tm2.write(allseg3)

# Run initial setup
display(terrain, values)
#Choose 'roll dice!' pin
roll = Pin(8, mode=Pin.IN, pull=Pin.PULL_UP)
#roll.irq(trigger=Pin.IRQ_RISING,handler=ISR_roll)
roll.irq(trigger=Pin.IRQ_FALLING,handler=ISR_roll_start)
#Now, the main game loop
def main(x):
    global blinkState
    if current_dice1 > 0: #Will always be more than zero if the dice has been rolled at least once, e.g. the game has begun.
        if blinkState == True:
            display(terrain, values)
            roll.irq(trigger=Pin.IRQ_FALLING,handler=ISR_roll_start)
            blinkState = False
        else:
            if currentRoll == 7:
                temp_values = []
                temp_values.extend(values)
                for i in temp_values:
                    if i[0] == int('01111011', 2):
                        i[0] = i[0] - 16
                    else:
                        i[0] = i[0] - 8
                display(terrain, temp_values)
                for i in temp_values:
                    if i[0] == int('01101011', 2):
                        i[0] = i[0] + 16
                    else:
                        i[0] = i[0] + 8
                blinkState = True
            else:    
                temp_values = []
                temp_values.extend(values)
                for i in indices:
                    temp_values[i] = [0,0] 
                display(terrain, temp_values)
                blinkState = True

        

autoroller = Timer(mode=Timer.PERIODIC, period=250, callback=main)
#sleep_goto_dormant_until_edge_high(6);
while True:
    pass