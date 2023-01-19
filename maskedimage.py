import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--i", type=str)
parser.add_argument("--m", type=str)
args = parser.parse_args()
image = args.i
mask = args.m

img=cv2.imread(os.path.join(os.getcwd(),image))
msk=cv2.imread(os.path.join(os.getcwd(),mask))

out = cv2.bitwise_and(img, msk)
cv2.imwrite("masked_image.png", out)