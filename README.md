# Detecting Photoshopped Faces 
## Using DockerHub

1. Pull the image from my repository:

`docker pull jull1ll/fal_detector`

2. Run the container:

`docker run jull1ll/fal_detector`

## Building the image using local machine
1. Clone the project:


`git clone https://github.com/JulianKo1/dl_project.git`

2. Go to the folder of the newly cloned project:

`cd <YOUR PATH>`

3. Build the image:

`docker build -t faldetectordemo .`

4. Run the container:

`docker run faldetectordemo`
## Related links:
+ [Project page](https://paperswithcode.com/paper/detecting-photoshopped-faces-by-scripting) on Papers With Code

+ [Link](https://github.com/PeterWang512/FALdetector) to original repository
