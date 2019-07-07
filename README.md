credit to https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python, and lots of other people who've done all the real work preceeding this


#### random notes

- added -cthresh option to use a lower confidence level
    - after my initial image stitching test failed, setting confidence from 1.0 to 0.8 succeeded


this cropping results in a super narrow panorama..
```bash
python3 stitch.py --images images/rug   --output rug-cropped.png --crop 1
```
to be fair, the author said it was a hack! so we just don't use it..
```bash
python3 stitch.py --images images/rug  --output rug.png
```
<img src="rug01.jpg" width="64px"/>
<img src="rug02.jpg" width="64px"/>
<img src="rug03.jpg" width="64px"/>
<img src="rug04.jpg" width="64px"/>
<img src="rug05.jpg" width="64px"/>
<img src="rug06.jpg" width="64px"/>
<img src="rug07.jpg" width="64px"/>
<img src="rug08.jpg" width="64px"/>
<img src="rug09.jpg" width="64px"/>
<img src="rug10.jpg" width="64px"/>


<img src="rug.png" alt="stitched rug panorama" title="rug"/>


    https://stackoverflow.com/questions/40088222/ffmpeg-convert-video-to-images/40090033
