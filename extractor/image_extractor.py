#!/usr/bin/env python

import cv2 
import argparse
import pathlib


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--video",  type=str, required=True,  help="path to input video")
ap.add_argument("-o", "--output",  type=str, required=True, help="path to the output folder")
ap.add_argument("-n", "--everyn",  type=int, required=False, help="path to the output image", default=30)
args = vars(ap.parse_args())

video_file=args["video"]
output_dir=args["output"]
everyN=args["everyn"]



vid = cv2.VideoCapture(video_file)
o_path = pathlib.Path(output_dir)
o_path.mkdir(parents=True, exist_ok=True)

seen = -1
success = 1
while success: 
    success, image = vid.read() 
    seen += 1
    if success and (seen % everyN) == 0:
        o_file='{0}/frame{1}.jpg'.format(output_dir,str(seen).zfill(5))
        
        cv2.imwrite(o_file, image) 
#        cv2.imshow( 'image{}'.format(seen), image)
        cv2.imshow( 'image', image)
        print('file written: ', o_file)
        print("press any button to continue")
        b=cv2.waitKey(0)


