#!/bin/bash


#Take one minute chunk of video starting after 1:08
oName=day2a
ffmpeg -ss 00:01:08 -i ~/rov_videos_day2/2019-07-13_09.59.05.mkv -t 00:01:00 -vcodec copy videos/${oName}.mkv

#Extract image every 0.5 seconds. crop 128 pixels from left and bottom (probably)
# frames per second... (images per second)
FPS=1
mkdir images/${oName}
ffmpeg -i videos/${oName}.mkv -qscale:v 2 -vf "crop=in_w-128:in_h-128:128:0,fps=${FPS}" images/${oName}/%05d.jpg

#Move images into groups of no more than 10..
groups=$(( $(ls images/${oName} | wc -l) / 10))
for i in $(seq -w 0000 $groups)
do 
 mkdir images/${oName}_${i} 
 mv images/${oName}/${i}*.jpg images/${oName}_${i} 
done

#Try to stitch each group
for i in $(seq -w 0000 $groups)
do 
 oLog=stitched_output/${oName}_${i}.md
 which tee >/dev/null && TEE=true
 if [ $TEE ]; then
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
        echo "<img src='${img}' width='64px' align='left' />" 
    done > $oLog

    echo "<img src='stitched_output/${oName}_${i}.png' alt='stitched output for ${oName}' title='stitched' />" >> $oLog
 fi
done

