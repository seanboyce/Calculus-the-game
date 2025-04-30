## Resistor sizes

I've supplied two versions of the kicad and production files. The default version uses 0402 (1005 metric) components. Many people would find these hard to hand solder -- they are about the size of two grains of salt. If you want something easier to solder, check out the 0603 version -- there's a zip file with the KiCAD and production files. Strictly speaking, it's not tested (I made the 0402 version). However, the only thing I did is change the resistor footprints, so it should be fine. 

## Note the production files are in metric units

If you need to switch it to some other system, you'll need to open the KiCAD files and generate your own production files (it's very easy)

Also note these boards have a little note in silkscreen on the back with my name and where they were designed. It's meant to be a kind note that I cared to design these for you, and I hope you enjoy them.

You may remove it if you wish. Just open up the PCB in KiCAD, select the text, and press delete. Then re-export the production files.

## KiCAD files

There are some custom footprints I think? Not sure how that gets handled. Let me know if anything outright breaks.

The routing is still pretty YOLO in this version (although less bad than the cheap version), feel free to clean it up. I tried to mostly keep traces off the top of the board so it looks clean.
