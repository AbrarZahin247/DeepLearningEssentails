import argparse
import re
import os
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--s")
parser.add_argument("--d")
parser.add_argument("--size", type=str)

args = parser.parse_args()

source = args.s
dest = args.d
size = (args.size).split(",")
size=(int(size[0].replace("(","")),int(size[1].replace(")","")))
#print(size)
#dest=re.escape(dest)

print(source,dest,size)


def resize(source,dest,size):
    #source="D:\\CEGIS\\Drone_Image_Processing\\UAV Images\\renamed_files\\images"
    #dest="D:\\CEGIS\\Drone_Image_Processing\\UAV Images\\renamed_files\\images\\small_res"
    if size == None or size=="auto":
        h,w=get_min_width_height(source)
        size=(h,w)
    #print(size[0],size[1])
    dest=check_create_directory(dest)
    for file in os.listdir(source):
        print(file)
        filename = os.path.join(source,file)
        src = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        output = cv2.resize(src, (size[1],size[0]))
        filename = os.path.join(dest,file)
        cv2.imwrite(filename,output)

def get_min_width_height(location):
    min_size=[9999999999999,999999999999]
    for file in os.listdir(location):
        img_file=os.path.join(location,file)        
        img = cv2.imread(img_file)
        if len(img)>0:
            h,w,c = img.shape  
            print(h,w)      
            if h<min_size[0]:
                min_size[0]=h
            if w<min_size[1]:
                min_size[1]=w
    if(min_size[0]==9999999999999):
        min_size[0]=None
    if(min_size[1]==9999999999999):
        min_size[1]=None
    return min_size[0],min_size[1]

def check_create_directory(dest=""):
    parent=os.getcwd()
    if(dest != None and os.path.exists(dest)):
        return dest
    dir_path=os.path.join(parent,"reshaped_images")
    if(not os.path.exists(dir_path)):
        os.mkdir(dir_path)
    return dir_path  

    
resize(source,dest,size)


