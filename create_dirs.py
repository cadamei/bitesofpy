#!python3
import os

# Create target Directory if don't exist
for dirName in range(0, 201):
    if not os.path.exists(str(dirName)):
        os.mkdir(str(dirName))
        print("Directory ", str(dirName), " Created ")
    else:
        print("Directory ", str(dirName), " already exists")
