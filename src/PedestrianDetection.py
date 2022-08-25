# import libraries and dependencies
from PIL import Image
import glob

# import train dataset

image_list = []
for filename in glob.glob(r'C:\Users\monic\OneDrive\Desktop\MS Thesis\PedestrianDetection\data\img1/*.jpg'):
    im=Image.open(filename)
    image_list.append(im)

# display first and last images to see if files are read correctly
image_list[0].show()
image_list[-1].show()

