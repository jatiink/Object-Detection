# Auto Object Detection
In this project, I will explore images to find obect by removing background.

## INSTRUCTIONS
### This project requires the following libraries :
•	[Numpy](https://numpy.org/)<br />
•	[Cv2(OpenCV)](https://docs.opencv.org/4.x/)<br />
• [Rembg](https://github.com/danielgatis/rembg)<br />
• [Argparse](https://docs.python.org/3/library/argparse.html)<br />

### Please ensure you have installed the following libraries mentioned above before continuing.
 
<details open>
<summary>Usage</summary>

### CLI

To Run directly in command line.
#### First clone this repositories and open cmd and then type:
```
python main.py --source "image path"
```

You have to select area from where you want to detect object.<br />
You will get full image with object outlined.

#### To view only object without Background:
```
python main.py --source "image path" --rembg True
```

#### To Save only object without Background:
```
python main.py --source "image path" --save-rembg True
```

#### To Save full image with object oulined:
```
python main.py --source "image path" --save-image True
```
All image will open in separate window.<br />
To Quit in opened window "Press `q`"<br />
To view normal image after viewing oulined object image "Press `c`"<br />
To view how project will work `See Demo.mp4`

</details>
