from  pathlib import Path
import subprocess
import os

#set local path and upcoming variables
inputpath = Path.cwd()
check = []
realpaths = []
spritepath = []
framerate = 0
manual_id = []

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

def getthemall(name): #Gathers every sprites if the labelled option is chosen
    global realpaths
    global spritepath
    for animsprite in inputpath.glob("input/cookie*x2_" + name +"_????.png"):
        spritepath.append(animsprite)
    for x in spritepath:
        realpaths.append(str(x))
    realpaths = ' '.join(realpaths)

def getittogether(idlist): #gathers every sprites incated through the label-less option
    global realpaths
    global spritepath
    for x in idlist:
        for animsprite in inputpath.glob("input/cookie*x2_" + x + ".png"):
            spritepath.append(animsprite)
    for y in spritepath:
        realpaths.append(str(y))
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
    print("now give the FPS value from the associated aniinfo.plist file. (please only add 3 numbers after the dot.)")
    plist_framerate = float(input())
    dothemath(plist_framerate)
    png_2_gif()

def unlabelled_sprites(): #funnction that proceeds the compuilation of sprites if it was not labelled beforehand.
    x=1
    check_png()
    output_clear()
    print("the sprites are unlabelled, hope you have the associated aniinfo.plist close")
    global manual_id
    print("Please type the four digit number of the file, make sure to add 1 to the number shown on the plist you want to assemble")
    ident = input()
    manual_id.append(ident)
    while x == 1:
        output_clear()
        print("current digit listed : ")
        print(manual_id)
        print("Please type the four digit number of the file, make sure to add 1 to the number shown on the plist you want to assemble")
        print("type 'done' if you're done with listing the ids")
        ident = input()
        if ident == "done":
            break
        manual_id.append(ident)
    getittogether(manual_id)
    print("now give the FPS value from the associated aniinfo.plist file. (please only add 3 numbers after the dot.)")
    plist_framerate = float(input())
    dothemath(plist_framerate)
    png_2_gif()


def base_check(): #checking if the input folder is there or if its empty.
    for x in inputpath.glob("input/*"):
        check.append(x)
    if len(check) == 0:
        print("Seems like the input folder is empty or non-existant, please create the input folder (just call it input) and place the sprites (as pngs), or gifs in the input folder, and launch the program again.")
        quit()

def program_check(program):  #Checks if ImageMagick and Gifsicle are installed on the device
    try:
        subprocess.run(program, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"it seems that {program[0]} is not installed on your system or is not located in the PATH, please install it and try again.")
        print("for more informatiion on what is the PATH, please check the tutorial video linked on the github page.")
        quit()

def intro(): #intro of the program
    print("Type 1 if the sprites in the input folder are labelled, if not, type 2, to compile gifs, type 3.")
    option = int(input())
    match option:
        case 1:
            labelled_sprites()
        case 2:
            unlabelled_sprites()
        case 3:
            combine_gif()
        case _:
            quit()

def dothemath(fps): #calculates the fps value for the gif
    global framerate
    framerate = ((60*fps)*60)/25

def png_2_gif(): #turns the selection of pngs into a single gif through ImageMagick
    print("please give the output name for the file")
    outputname = input()
    outputname = outputname.replace(" ", "_")
    if outputname.find('.gif') == -1:
        outputname = outputname + ".gif"
    command = f"magick {realpaths} -set delay {str(framerate)} -loop 0 -set dispose 2 -trim -layers trim-bounds -channel A -ordered-dither o8x8 {outputname}"
    run_imagemagick(command)
    print("the gif should now be located in the root folder, thanks for using the program!")

def run_imagemagick(cmd): # runs ImageMagick
    print(cmd)
    subprocess.call(cmd, shell=True)

output_clear()
print("Cookie-Gif-Creator")
print("By AGamer360 for the CookieRun Wiki")
print()
base_check()
program_check(["magick", "--version"])
program_check(["gifsicle", "--version"])

intro()
