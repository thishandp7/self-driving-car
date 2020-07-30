# Self-Driving Car DNN Model
 - A Deep Neural Network model based on Nvidia’s proposed Convolutional Neural Network architecture for self-driving cars.
 - The model was trained using the imaged collected from Udacity’s Self Driving car simulator.
 - The goal of this project is to predict the correct steering angle while driving.
 
## Data collection
 - Approximately 18,000 images were collected from the Udacity’s Self Driving car simulator by manually driving the car around the map.
 - Always tried to keep the car in the middle of the road while collecting data from the simulator
 - Tried to have a fair balance between the amount of left and right turns made in the simulator to collect an evenly balanced data for the steering angle
 - The car in the simulator is equipped with three cameras: left, right, and center, also the simulator records the steering angle, speed, throttle, and brake for each image. 
 The speed, throttle and brake data were later removed since the focus of the project is to predict the steering anlge.

## Data analysis
 - Visualized the data using histograms to get a clear view of the data
 - The simulator had mostly straight roads, and this resulted in a significantly high volume of steering angles with 0. Therefore, most of the data with 0 steering angle were removed to avoid the model becoming biased towards driving straight.
 - Data was then split into training and validation sets. 80% for the training set, and the rest 20% was used for validation.

## Data pre-processing
 - Removed unnecessary data from the images such as pixels above the road and pixels describing the car’s hood. This helped focusing only on essential data, such as the edge of the road.
 - Color space for the images was converted to YUV from RGB since Nvidia recommends the YUV color space for thier recommened DNN architecure.
 - Gaussian blur was applied to all the images to smooth and reduce the noise
 - Images were resized to a reasonably smaller size to speed up the computation
 - All the images were normalized by dividing each pixel value by 255

## Data agumentation
 - Approximately 30,000 more training images were created by agumenting the original data
 - A generator function was created to make new augmented images as the model gets trained instead of storing a large number of data locally and then using it for traning.
 - Augmented images were created by using the original images with combinations of following operations:
    - Zoomed the image by 30%
    - Panned the image by 10% in one of the four direction
    - Randomly increased or decreased the image brightness by 20%
    - Fliped the images horizontally and update the corresponding steering angle to match the flip

## Nvidia model
- The CNN architecture proposed by Nvidia has about 27 million connection as 250 thouansd parameters.
- Following image is taken from the [paper](https://developer.nvidia.com/blog/deep-learning-self-driving-cars/) publish by Nvidia.
<p align="center">
  <img src="https://developer.nvidia.com/blog/parallelforall/wp-content/uploads/2016/08/cnn-architecture-624x890.png" width="400">
</p>

## WebSocket Server
