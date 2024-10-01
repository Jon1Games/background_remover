from rembg import remove
from PIL import Image
import sys
import os

# Variables
skip = False
input_path = ""
output_path = ""
valid = False

# Checking for help
if sys.argv[1] == "-?" or sys.argv[1] == "--?" or sys.argv[1] == "?" or sys.argv[1] == "help" or sys.argv[1] == "-help" or sys.argv[1] == "--help":
    print("-i <input_path>  | Input path")
    print("-o <output_path> | Output path")

# Collecting arguments
for i in range(1, len(sys.argv)):
    if skip == True:
        skip = False
    elif sys.argv[i] == "-i":
        input_path = sys.argv[i+1]
        skip = True
    elif sys.argv[i] == "-o":
        output_path = sys.argv[i+1]
        skip = True
    elif sys.argv[i] == "-test":
        pass
    else:
        print("unknown argument, use -? to get more informations")

if os.path.exists(input_path) and os.path.isfile(input_path):
    if os.path.exists(output_path):
        if input("override? [y/n]: ") == "y":
            valid = True
    else:
        valid = True
else:
    print("The path of the input file does not exist!")
    
if valid == True:
    inp = Image.open(input_path)
    out = remove(inp)
    out.save(output_path)