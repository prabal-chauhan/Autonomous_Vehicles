# Lane_detection
### In this project, our goal is to:

* Find the lanes in the images.
* Apply smoothing to draw only smooth lanes.

### Computer Vision:

* Computer vision is a field of computer science that works on enabling computers to see, identify and process images in the same way that human vision does, and then provide appropriate output. It is like imparting human intelligence and instincts to a computer. In reality though, it is a difficult task to enable computers to recognize images of different objects.
* Computer vision is closely linked with artificial intelligence, as the computer must interpret what it sees, and then perform appropriate analysis or act accordingly

#### How computer vision works

Computer vision works in three basic steps:

1. Acquiring an image.

2. Processing the image.

3. Understanding the image.

```
The Pipeline:

The steps below represents the working pipeline of Lane Detection Model:-

1. Load the lane image/video.
2. Convert the image into HSV(Greyscale).
3. Remove noise from the image using Gaussian Blur Filter.
4. Get the edges in the images using Canny Edge Detection.
5. Remove edges outside of the (Region of Interest).
6. Find Lines using Hough Line Transform Algorithm.
7. Find the coordinates of the Lanes.
8. Draw Lanes.

```
---
How to run this Project:-

1. Download a Text Editor (i.e Atom https://atom.io/)
2. Download Anaconda Distribution Framework (integrated with Python 3.xx)
3. Extract the Repository (i.e. Clone..Download..Extract)
4. Install some Libraries:
    `pip install opencv-contrib-python`
    `pip install numpy`.
5. `test_image.jpg` is the image that we can run in this project and Extract `test2_part1.rar` which contain video to detect lanes.
6. Open `cmd` to run cd Filename>>Hough Transform.py
---

