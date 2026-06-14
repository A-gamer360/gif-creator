#importing libraries
import argparse
from  pathlib import Path
import subprocess

# setting up the Arguments
inputpath = Path.cwd()

parser = argparse.ArgumentParser(
    prog="Cookie Gif Generator", description="Compiles gifs for a specific cookie game. requires the files to be labelled, and requires imagemagick and gifsicle to be in PATH.", epilog="Made by AGamer360 for cookierun.wiki")
parser.add_argument('-l', '--label', help="Label of the type of gif", type=str, action="store", required=True)
parser.add_argument('-fps', help="framerate of the gif from plist '3 numbers of precision required'", type=float, action="store", required=True)
parser.add_argument('-o', '--output', help="Output name", type=str, action="store", required=True)

#collects the arguments and parse them into variables + creation of said variables
args = parser.parse_args()
fps = ((60*args.fps)*60)/25
outputname = args.output
anilabel = args.label.replace(" ", "_")
spritepath = []
realpaths = []
#debug stuff
print("framerate is : ")
print(fps)
# print("label is : " + anilabel)
# for sprites in inputpath.glob("input/*.png"):
#    print(sprites)

# searching for the correctly labelled sprites
for animsprite in inputpath.glob("input/cookie*x2_" + anilabel +"_????.png"):
    # print(animsprite)
    spritepath.append(animsprite)
#converting path into strings
for x in spritepath:
    realpaths.append(str(x))

realpaths = ' '.join(realpaths)
# print(realpaths)

# imagemagick time

magickcommand = "magick " + realpaths + " -set delay " + str(fps) + " -loop 0 -set dispose 2 -trim -layers trim-bounds -channel A -ordered-dither o8x8 " + outputname

subprocess.call(magickcommand, shell=True)
