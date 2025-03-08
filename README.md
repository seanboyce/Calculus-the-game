# Calculus-the-game
An electronic strategy board game about mining an asteroid and barter. It is also fully compatible with Settlers of Catan. So if you already own that game, you can play it using this board if you wish (using the cards and pieces). The holders of the Catan copyright generously allow you to make one (1) handmade copy of their game for personal use. A practical thing to do is buy their game, and use the included pieces and cards (although please note the pieces will only physically fit the full-size version). For more information, please visit this link: https://www.catan.com/guidelines-dealing-intellectual-property-catan

Out of respect for their IP (and also for fun), my own game will be sci-fi themed and will not use or refer to their IP beyond this point. 

The name of the game is Calculus, in the sense of a "stone, or concretion of material". In this case, an asteroid in deep space! You are one of up to four corporations that are racing to exploit this valuable asteroid. The corporation that reaches a certain level of development (10 development points) first will own this tiny piece of the sky. This is the object of the game. Besides the four corporations, a mysterious hacker has made their home here, and is bound to interfere with your plans...

# Status
There are two versions of this game:

1. The cheap version (complete) -- this version only has one PCB, although you will need 3 units to build the game. It is very cheap to manufacture, but a bit small and cramped to play. It is missing a little polish overall. Notably, trade ports are not electronic (I use magnetic tokens), the landing zone (unproductive tile) is limited to being in the center of the board, and there's no MCU on the board itself -- it needs to be added externally and wired in to the inputs. You'll also need to hack in a button. Still, it's very cheap to make and perfectly serviceable.
2. The full-size version (waiting for boards, firmware in progress) -- this one is much larger (more than double the size). It uses two PCBs: a large one (you will need 3), and a small one (you will need 1). The small PCB has space for an MCU, making the final board much more self-contained. It is also an active game tile -- the landing zone (unproductive tile) can be randomized like other tiles. Trade ports are randomized and represented by RGB LEDs like resource tiles. There are also some cosmetic improvements like a proper button and nicer lines.

Other than noted above, both versions play the same.

# Firmware

Besides the assembled PCBs, you will need to load firmware to the main microcontroller (an RP2040). This is pretty easy and can be done over USB. The firmware is heavily commented -- this is so you can make 'house' modifications to the game mechanics, to change the rules if you want. You could even design a completely new game!

# Notes on Assembly

Assembling the PCBs will require that you are comfortable with surface-mount soldering. It's not nearly as hard as it looks. You'll need solder paste and a hot air rework station though. If you don't have these, check if there's a hackerspace near you. They probably will!

# BOM (TODO)

# Images of Completed Board (small version)
![Photo of the sompleted small version of the game](https://raw.githubusercontent.com/seanboyce//Calculus-the-game/refs/heads/main/calculus_small/calculus_small_built.JPG)
