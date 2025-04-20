## Make sure to use the right version of the firmware for your game.

Unlike some of my other projects, this is purely written in micropython rather than AVR assembly. I wanted it to be more accessible to beginners, and the extra power use by the RP2040 is pretty irrelevant in the context of all the LEDs.

The firmware uses the tm1640 driver from here: https://github.com/mcauser/micropython-tm1640. The licence for that code is different from the rest of this project, and defined in that file.

To learn how the firmware works, your best bet is to read the source code in main.py for the full version of the game. It's heavily commented.
