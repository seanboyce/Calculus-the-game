# Calculus-the-game
An electronic strategy board game about mining an asteroid and barter.

# Status
There are two versions of this game:

1. The cheap version -- this version only has one PCB, although you will need 3 units to build the game. It is very cheap to manufacture, but a bit small and cramped to play. It is missing a little polish overall. Notably, trade ports are not electronic (I use magnetic tokens), the landing zone (unproductive tile) is limited to being in the center of the board, and there's no MCU on the board itself -- it needs to be added externally and wired in to the inputs. You'll also need to hack in a button. Still, it's very cheap to make and perfectly serviceable.
2. The full-size version -- this one is much larger (more than double the size). It uses two PCBs: a large one (you will need 3), and a small one (you will need 1). The small PCB has space for an MCU, making the final board much more self-contained. It is also an active game tile -- the landing zone (unproductive tile) can be randomized like other tiles. Trade ports are randomized and represented by RGB LEDs like resource tiles. There are also some cosmetic improvements like a proper button and nicer lines.

Other than noted above, both versions play the same.
