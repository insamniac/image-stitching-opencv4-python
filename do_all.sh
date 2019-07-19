#!/bin/bash


#Take one minute chunk of video starting after 1:08
oName="${1:-00100}"

#ffmpeg -ss 00:01:08 -i ~/rov_videos_day2/2019-07-13_09.59.05.mkv -t 00:01:00 -vcodec copy videos/${oName}.mkv

#Extract image every 0.5 seconds. crop 128 pixels from left and bottom (probably)
# frames per second... (images per second)
FPS=${2:-1}
mkdir images/${oName}
ffmpeg -i videos/${oName}.MTS -qscale:v 2 -vf "rotate=90,scale=1024:-1,fps=${FPS}" images/${oName}/%05d.jpg

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
    oDir="stitched_output/${oName}"
    mkdir $oDir
 oLog=${oDir}/${oName}_${i}.md
 which tee >/dev/null && TEE=true
 if [ $TEE ]; then
     echo writing script output to $oLog
     echo '```bash' > $oLog
     time python3 stitch.py --nodisplay --images images/${oName}_${i} --output ${oDir}/${oName}_${i}.png | tee -a $oLog
     echo '```' >> $oLog
 else
     echo > $oLog
     time python3 stitch.py --nodisplay --images images/${oName}_${i} --output ${oDir}/${oName}_${i}.png 
 fi

 if [[ $(ls images/${oName}_${i} 2>/dev/null | wc -l) -gt 0 ]] ; then
    for img in $(ls images/${oName}_${i}/)
    do
        echo "<img src='../../images/${oName}_${i}/${img}' width='64px' align='left' />" 
    done >> $oLog

    echo "<img src='${oName}_${i}.png' alt='stitched output for ${oName}' title='stitched' />" >> $oLog
 fi
done

