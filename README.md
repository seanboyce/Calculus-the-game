# Calculus-the-game
An electronic strategy board game about mining an asteroid and barter. It is also fully compatible with Settlers of Catan. So if you already own that game, you can play it using this board if you wish (using the cards and pieces). The holders of the Catan copyright generously allow you to make one (1) handmade copy of their game for personal use. A practical thing to do is buy their game, and use the included pieces and cards (although please note the pieces will only physically fit the full-size version). For more information, please visit this link: https://www.catan.com/guidelines-dealing-intellectual-property-catan

Out of respect for their IP (and also for fun), my own game will be sci-fi themed and will not use or refer to their IP beyond this point. 

The name of the game is Calculus, in the sense of a "stone, or concretion of material". In this case, an asteroid in deep space! You are one of up to four corporations that are racing to exploit this valuable asteroid. The corporation that reaches a certain level of development (10 infrastructure points) first will own this tiny piece of the sky. This is the object of the game. Besides the four corporations, a mysterious hacker has made their home here, and is bound to interfere with your plans...

# Status
There are two versions of this game:

1. The cheap version (complete) -- this version only has one PCB, although you will need 3 units to build the game. It is very cheap to manufacture, but a bit small and cramped to play. It is missing a little polish overall. Notably, trade ports are not electronic (I use magnetic discs), the landing zone (unproductive tile) is limited to being in the center of the board, and there's no MCU on the board itself -- it needs to be added externally and wired in to the inputs. You'll also need to hack in a button. Still, it's very cheap to make and perfectly cromulent.
2. The full-size version (boards arrived and assembled, firmware in progress) -- this one is *much larger* (more than double the size). It uses two PCBs: a large one (you will need 3), and a small one (you will need 1). The small PCB has space for an MCU, making the final board much more self-contained. It is also an active game tile -- the landing zone (unproductive tile) can be randomized like other tiles. Trade ports are randomized and represented by RGB LEDs like resource tiles. There are also some cosmetic improvements like a proper button and nicer lines. One tradeoff is thst the firmware is a bit more convoluted to be able to control all those LEDs -- there are 388 (!) LEDs on the board when you count up all the RGB LEDs and two digit 8-segment displays.

Other than noted above, both versions play the same. It's expected that you power the game via a USB battery bank of some sort. Like the kind you use to recharge phones. However, you can power it from any USB port or 5V source.

Additional differences: The smaller board is intended to be attached above a small project box or similar. This serves the dual purpose of housing a microcontroller, and fixing the 3 PCBs firmly in place. The larger board has all those electronics integrated, and is meant to rest on a table. I've left holes in the PCB in case you want to bolt it to something, but it is not necessary. The smaller board requires custom pieces -- hex spacers, bolts, and nuts colored with a permanent marker work fine. The full size board can be played with pieces from a Catan set, or you can make your own.

# Firmware

Besides the assembled PCBs, you will need to load firmware to the main microcontroller (an RP2040). This is pretty easy and can be done over USB. The firmware is heavily commented -- this is so you can make 'house' modifications to the game mechanics, to change the rules if you want. You could even design a completely new game!

# Notes on Assembly

Assembling the PCBs will require that you are comfortable with surface-mount soldering. It's not nearly as hard as it looks. You'll need solder paste and a hot air rework station though. If you don't have these, check if there's a hackerspace near you. They probably will!

# BOM (TODO)

# Images of Completed Board (cheap version)
![Photo of the completed small version of the game](https://raw.githubusercontent.com/seanboyce//Calculus-the-game/refs/heads/main/calculus_small/calculus_small_built.JPG)

# Images of Completed Board (full version)
![Photo of the completed full version of the game](https://raw.githubusercontent.com/seanboyce//Calculus-the-game/refs/heads/main/calculus_full/unpowered.JPG)
