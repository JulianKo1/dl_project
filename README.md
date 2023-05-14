# Detecting Photoshopped Faces 
## Using DockerHub

1. Pull the image from my repository:

`docker pull jull1ll/faldetectordemo`

2. Run the container:

`docker run jull1ll/faldetectordemo`

## Building the image using local machine
1. Clone the project:


`git clone https://github.com/JulianKo1/dl_project.git`

2. Go to the folder of the newly cloned project:

`cd <YOUR PATH>`

3. Build the image:

`docker build -t faldetectordemo .`

4. Run the container:

`docker run faldetectordemo`

## Outputting results to your machine
1. Figure out container's id:

`docker ps -a`

2. Copy folder with results to your machine:

`docker cp <container_id>:./out/ <YOUR PATH>`

### Results folder contents

Folder contains your results as well as out1 and out2 (my results)

## Related links:
+ [Project page](https://paperswithcode.com/paper/detecting-photoshopped-faces-by-scripting) on Papers With Code

+ [Link](https://github.com/PeterWang512/FALdetector) to original repository
