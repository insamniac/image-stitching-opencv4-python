credit to https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python,
https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/
and lots of other people who've done all the real work preceeding this



### stitch the floor

*Note that the original video file isn't included in this repository.*

Take one minute chunk of video starting after 1:08
```bash
oName=day2a
ffmpeg -ss 00:01:08 -i ~/rov_videos_day2/2019-07-13_09.59.05.mkv -t 00:01:00 -vcodec copy videos/${oName}.mkv
```

Extract image every 0.5 seconds. crop 128 pixels from left and bottom (probably)
```bash
# frames per second... (images per second)
FPS=1
mkdir images/${oName}
ffmpeg -i videos/${oName}.mkv -qscale:v 2 -vf "crop=in_w-128:in_h-128:128:0,fps=${FPS}" images/${oName}/%05d.jpg
```

Move images into groups of no more than 10..
```bash
groups=$(( $(ls images/${oName} | wc -l) / 10))
for i in $(seq -w 0000 $groups)
do 
 mkdir images/${oName}_${i} 
 mv images/${oName}/${i}*.jpg images/${oName}_${i} 
done
```

Try to stitch each group
```bash
for i in $(seq -w 0000 $groups)
do 
 oLog=stitched_output/${oName}_${i}.md
 which tee >/dev/null && TEE=true
 if [ $TEE ]; then
     echo writing script output to $oLog
     echo '```bash' > $oLog
     time python3 stitch.py --nodisplay --images images/${oName}_${i} --output stitched_output/${oName}_${i}.png | tee -a $oLog
     echo '```' >> $oLog
 else
     echo > $oLog
     time python3 stitch.py --nodisplay --images images/${oName}_${i} --output stitched_output/${oName}_${i}.png 
 fi

 if [[ $(ls images/${oName}_${i} 2>/dev/null | wc -l) -gt 0 ]] ; then
    for img in $(ls images/${oName}_${i}/)
    do
        echo "<img src='../images/${oName}_${i}/${img}' width='64px' align='left' />" 
    done > $oLog

    echo "<img src='${oName}_${i}.png' alt='stitched output for ${oName}' title='stitched' />" >> $oLog
 fi
done

```

cleanup (delete all/most of the mess we just made)
```bash
rm -Rf images/DIRNAME* videos/DIRNAME* stitched_output/DIRNAME*
```




### other random notes

- added --nodisplay option to squelch the image popup
    - useful when running in a loop or inside a script

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
<img src="images/rug/rug01.jpg" width="64px" align="left" />
<img src="images/rug/rug02.jpg" width="64px" align="left" />
<img src="images/rug/rug03.jpg" width="64px" align="left" />
<img src="images/rug/rug04.jpg" width="64px" align="left" />
<img src="images/rug/rug05.jpg" width="64px" align="left" />
<img src="images/rug/rug06.jpg" width="64px" align="left" />
<img src="images/rug/rug07.jpg" width="64px" align="left" />
<img src="images/rug/rug08.jpg" width="64px" align="left" />
<img src="images/rug/rug09.jpg" width="64px" align="left" />
<img src="images/rug/rug10.jpg" width="64px" align="left" />


<img src="rug.png" alt="stitched rug panorama" title="rug"/>


    https://stackoverflow.com/questions/40088222/ffmpeg-convert-video-to-images/40090033



## test script to split videos


```bash
>python3 vproc.py videos/day2a.mkv 30

file written: videos/day2a.mkv_frame0.jpg
file written: videos/day2a.mkv_frame30.jpg
file written: videos/day2a.mkv_frame60.jpg
file written: videos/day2a.mkv_frame90.jpg
file written: videos/day2a.mkv_frame120.jpg
file written: videos/day2a.mkv_frame150.jpg
file written: videos/day2a.mkv_frame180.jpg
file written: videos/day2a.mkv_frame210.jpg
file written: videos/day2a.mkv_frame240.jpg
file written: videos/day2a.mkv_frame270.jpg
file written: videos/day2a.mkv_frame300.jpg
file written: videos/day2a.mkv_frame330.jpg
file written: videos/day2a.mkv_frame360.jpg
file written: videos/day2a.mkv_frame390.jpg
file written: videos/day2a.mkv_frame420.jpg
file written: videos/day2a.mkv_frame450.jpg
file written: videos/day2a.mkv_frame480.jpg
file written: videos/day2a.mkv_frame510.jpg
file written: videos/day2a.mkv_frame540.jpg
file written: videos/day2a.mkv_frame570.jpg
file written: videos/day2a.mkv_frame600.jpg
file written: videos/day2a.mkv_frame630.jpg
file written: videos/day2a.mkv_frame660.jpg
file written: videos/day2a.mkv_frame690.jpg
file written: videos/day2a.mkv_frame720.jpg
file written: videos/day2a.mkv_frame750.jpg
file written: videos/day2a.mkv_frame780.jpg
file written: videos/day2a.mkv_frame810.jpg
file written: videos/day2a.mkv_frame840.jpg
file written: videos/day2a.mkv_frame870.jpg
file written: videos/day2a.mkv_frame900.jpg
file written: videos/day2a.mkv_frame930.jpg
file written: videos/day2a.mkv_frame960.jpg
file written: videos/day2a.mkv_frame990.jpg
file written: videos/day2a.mkv_frame1020.jpg
file written: videos/day2a.mkv_frame1050.jpg
file written: videos/day2a.mkv_frame1080.jpg
file written: videos/day2a.mkv_frame1110.jpg
file written: videos/day2a.mkv_frame1140.jpg
file written: videos/day2a.mkv_frame1170.jpg
file written: videos/day2a.mkv_frame1200.jpg
file written: videos/day2a.mkv_frame1230.jpg
file written: videos/day2a.mkv_frame1260.jpg
file written: videos/day2a.mkv_frame1290.jpg
file written: videos/day2a.mkv_frame1320.jpg
file written: videos/day2a.mkv_frame1350.jpg
file written: videos/day2a.mkv_frame1380.jpg
file written: videos/day2a.mkv_frame1410.jpg
file written: videos/day2a.mkv_frame1440.jpg
file written: videos/day2a.mkv_frame1470.jpg
file written: videos/day2a.mkv_frame1500.jpg
file written: videos/day2a.mkv_frame1530.jpg
file written: videos/day2a.mkv_frame1560.jpg
file written: videos/day2a.mkv_frame1590.jpg
file written: videos/day2a.mkv_frame1620.jpg
file written: videos/day2a.mkv_frame1650.jpg
file written: videos/day2a.mkv_frame1680.jpg
file written: videos/day2a.mkv_frame1710.jpg
file written: videos/day2a.mkv_frame1740.jpg
file written: videos/day2a.mkv_frame1770.jpg
file written: videos/day2a.mkv_frame1800.jpg
file written: videos/day2a.mkv_frame1830.jpg
file written: videos/day2a.mkv_frame1860.jpg
file written: videos/day2a.mkv_frame1890.jpg
file written: videos/day2a.mkv_frame1920.jpg
```

