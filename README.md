# Introduction
An electronic strategy board game about mining an asteroid and barter. It is also fully compatible with Settlers of Catan. So if you already own that game, you can play it using this board if you wish (using the cards and pieces from the original). The holders of the Catan copyright also generously allow you to make one (1) handmade copy of their game for personal use. A practical thing to do is buy their game, and use the included pieces and cards (although please note the pieces will only physically fit the full-size version, see below). For more information on IP, please visit this link: https://www.catan.com/guidelines-dealing-intellectual-property-catan

Out of respect for their IP (and also for fun), my own game will be sci-fi themed and will not use or refer to their IP beyond this point. 

## Sci-Fi theme?
The name of the game is Calculus, in the sense of a "stone, or concretion of material". In this case, an asteroid in deep space! You are one of up to four corporations that are racing to exploit this valuable asteroid. The corporation that reaches a certain level of development (10 infrastructure points) first will own this tiny piece of the sky. This is the object of the game. Besides the four corporations, a mysterious hacker has made their home here, and is bound to interfere with your plans...

# Status
I still need to write up a manual and reference cards, do artwork for the game cards and maybe pieces. The electronics and firmware are in a finished state though.

There are two versions of this game, both complete:

1. The cheap version -- this version only has one PCB, although you will need 3 units to build the game. It is very cheap to manufacture, but a bit small and cramped to play. Call it a "travel version"! It is missing a little polish overall, and the firmware (while completely functional) is a little chaotic. Notably, trade ports are not electronic (I use magnetic discs), the landing zone (unproductive tile) is limited to being in the center of the board, and there's no MCU on the board itself -- it needs to be added externally and wired in to the inputs. You'll also need to hack in a button. Still, it's very cheap to make and perfectly cromulent.
2. The full-size version -- this one is *much larger* (more than double the size). It uses two PCBs: a large one (you will need 3), and a small one (you will need 1). The small PCB has space for an MCU, making the final board much more self-contained. The small board goes in the center and is also an active game tile -- the landing zone (unproductive tile) can be randomized like other tiles because of this. Trade ports are randomized and represented by RGB LEDs like resource tiles (or off for 3:1). There are also some cosmetic improvements like a proper button and nicer lines. I've also substantially cleaned up the firmware to control all those LEDs -- there are 388 (!) LEDs on the board when you count up all the RGB LEDs and two digit 8-segment displays. 

Other than noted above, both versions play the same. 

## Power
It's expected that you power the game via a USB battery bank. Like the kind you use to recharge phones. However, you can power it from any USB port or 5V source. Current consumption at 5v should be around 250mA for the cheap version, and a little higher for the full version (say 300mA)

## CPU
The cheap version of the game can use more or less any RP2040 based board. The original Pi Pico works fine. The full version specifically requires the XIAO RP2040 -- it's smaller and I needed the space.

## Structural
The boards for the cheap version are intended to be attached above a small project box or similar. This serves the dual purpose of housing a microcontroller, and fixing the 3 PCBs firmly in place. The larger board has all those electronics integrated, and is meant to rest on a table. I've left holes in the PCB in case you want to bolt it to something, but it's expected you use rubber feet held in place by 3mm bolts/nuts, like the type used in furniture. I find 10mm is a good height, you will need at least 8mm.

## Game Pieces
The cheap requires custom pieces -- hex spacers, bolts, and nuts colored with a permanent marker work fine. The full size board can be played with pieces from a Catan set, or you can make your own.

# Firmware
Besides the assembled PCBs, you will need to load firmware to the main microcontroller (an RP2040). This is pretty easy and can be done over USB. The firmware is heavily commented -- this is so you can make 'house' modifications to the game mechanics, to change the rules if you want. You could even design a completely new game!

# Notes on Assembly
Assembling the PCBs will require that you are comfortable with surface-mount soldering. It's not nearly as hard as it looks. You'll need solder paste and a hot air rework station though. If you don't have these, check if there's a hackerspace near you. They probably will! Right now it makes use of 0402 components. I'll redesign for 0603 or similar at some point -- this will be easier for beginners to solder.


# Image of Completed Board (full version)
![Photo of the completed full version of the game](https://raw.githubusercontent.com/seanboyce//Calculus-the-game/refs/heads/main/calculus_full/fullboard_power.JPG)

# Image of Completed Board (cheap version)
![Photo of the completed small version of the game](https://raw.githubusercontent.com/seanboyce//Calculus-the-game/refs/heads/main/calculus_small/calculus_small.JPG)

