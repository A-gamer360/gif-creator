import argparse
from  pathlib import Path
import subprocess
import os

#set local path and upcoming variables
inputpath = Path.cwd()
check = []
lists = {}
# function creation for easier code writing below.
def check_gif(): #checks the input folder if there's any gif inside'
    for x in inputpath.glob("input/*.gif"):
    check.append(x)
    if len(check) == 0:
        print("seems like the input folder does not contain any gif files. please input gif files into the input folder and launch the program again.")
        quit()

def check_png(): #checks the input folder if there's any png inside'
    for x in inputpath.glob("input/*.png"):
    check.append(x)
    if len(check) == 0:
        print("seems like the input folder does not contain any png files. please input png files into the input folder and launch the program again.")
        quit()

def output_clear(): #checks the operating system the program runs on to clear the terminal for easier reading
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def getthemall(str name): #Gathers every sprites if the labelled option is chosen
    print("files to get : " + name)
    for animsprite in inputpath.glob("input/cookie*x2_" + anilabel +"_????.png"):
        print(animsprite)
        spritepath.append(animsprite)
    for x in spritepath:
        realpaths.append(str(x))
    realpaths = ' '.join(realpaths)

def compile_gif(): #funciton that proceeds the compilation of all the gifs in the input folder
    check_gif()

def labelled_sprites(): #function that proceeds the compilation of sprites if it was labelled beforehand
    check_png()
    output_clear()
    print("since the sprites already labeled, this will make the job easier to do.")
    print("simply type the name of the sprites you want to compile into a gif.")
    filegroup_name = input()
    filegroup_name = filegroup_name.replace(" ", "_")
    getthemall(filegroup_name)

def unlabelled_sprites(): #funnction that proceeds the compuilation of sprites if it was not labelled beforehand.
    check_png()
    output_clear()

parser = argparse.ArgumentParser(
    prog="Manual Cookie Gif Generator",
    description="Manual compilation of sprites to make a gif, and gives more control over things. requires imagemagick and gifsicle to be installed on your system.",
    epilog="Made by AGamer360 for cookierun.wiki")

#checking if the input folder is there or if its empty
for x in inputpath.glob("input/*"):
    check.append(x)
if len(check) == 0:
    print("seems like the input folder is empty or non-existant, please put the sprites or gifs, and launch the program again.")
    quit()

#intro
print("Cookie-Gif-Creator")

print("This vesion will ask everything required as we go, please make sure the sprites are in the input folder, and that ImageMagick and Gifsicle are installed on your device before continuing.")
print()
print("Type 1 if the sprites in the input folder are labelled, if not, type 2, to compile gifs, type 3.")
if input = 1:
    labelled_sprites()
if input = 2:
    unlabelled_sprites()
if input = 3:!
    combine_gif()
else:
    quit()
