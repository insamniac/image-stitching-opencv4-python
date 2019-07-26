
### Using OpenDroneMap with ROV video


1. Create our project folders
```bash
mkdir project_1
cd project_1
mkdir images ortho textures
```


2. Find a section of video we want to use

GP020036.MP4  00:42 - 01:12 



3. Extract frames and crop the bottoms (the camera is in the way)
```bash
cd 
ffmpeg -i ../GP020036.MP4 -ss 00:42 -t 00:00:10 -vf "crop=in_w:in_h-384:0:0,fps=3" -qscale:v 1 images/frame%05d.jpg
```


4. Run ODM!

```bash
docker run -it --rm -v "$(pwd)/images:/code/images" -v "$(pwd)/ortho:/code/odm_orthophoto" -v "$(pwd)/textures:/code/odm_texturing" opendronemap/odm
```



5. Install meshlab
```bash
sudo apt-get install meshlab
meshlab
```


6. Your Turn!

- How do we make better meshes? 
- How can we combine them?
- [Camera Calibration|https://github.com/OpenDroneMap/CameraCalibration.git]




