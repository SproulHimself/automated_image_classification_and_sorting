# Automated Photograph Culling

### Abstract

This is my capstone project for Flatiron School.  I built two image classification models using convolutional neural networks, achieving accuracy scores of 91.5% and 87.8%. The models were combined into an application, currently in beta version.

----

### Motivation

The process of culling is used in every type of photography and is used by professionals and amateurs alike. Culling is simply the process of selecting the best images from a shoot to be edited and delivered to a client.

I am not a photographer, nor am I passionate about photography. But my current roommate is a passionate photographer who runs her own business. When she gets home from shoots, she has between 1000 to 2000 photos which she has to sort though manually. For my latest project I wanted to attempt to use deep learning techniques and python to build something that could save her time during the culling process.

<p align="center">
<img width="422"  src="https://user-images.githubusercontent.com/34200538/52924975-07c55b80-32fd-11e9-8216-39079ddbdadb.jpg">
</p>


#### Question?

* Can I use deep learning to classify photos based on specific features?

#### Goals:

* Identify photos that are blurry and not blurry
* Identify photos that do and don't contain people blinking
* Identify photos that are duplicate/similar (*Spoiler alert: ran out of time before I could complete this step)  
* Build a platform that automatically sorts photos for photographers to save time during the culling process





--------------
### Datasets

I curated my own custom datasets through combining several other datasets as well as scraping and cropping images.

* For the blurry model, I combined the [CERTH  image blur dataset](https://mklab.iti.gr/results/certh-image-blur-dataset/) and the [Portland State University, Blur image Dataset](https://riemenschneider.hayko.at/vision/dataset/task.php?did=382). I made this decision because I wanted the "blurry label" to be a more accurate representation of photographs that are good vs. bad. After combining the two sources, the dataset contains both artificially blurry and naturally blurry photos.

* For the blinking model, I started out with the [Closed Eyes In The Wild (CEW)](http://parnec.nuaa.edu.cn/xtan/data/ClosedEyeDatabases.html) dataset. Then, I manually went through and deleted photos which were incorrectly labeled or were of significantly poor quality. Lastly, using several Google image searches, I scraped and cropped roughly 500 images of both blinking and non-blinking eyes to make sure my dataset was large enough.


#### Preprocessing

After first attempting the project a go using a Jupyter Notebook, I soon realized that I needed some more processing power. Thus, this was my first exploration using a Google Colab Notebook. The preprocessing steps for the blurry model were far less intense than the blinking model.

For the blurry model, I resized the images to 224 x 224 pixels and rescaled them by 1.0/255.

<!-- Building the blinking model was much more of an iterative, trial and error process.
I chose 96 x 96 because many of the photos I was training/testing on were 24 x 24 and I wanted to preserve as much of the image quailty as possible -->

For the blurry model, I resized the images to 96 x 96 pixels and rescaled them by 1.0/255. This was done because I would be locating the faces in pictures and testing just the eyes.





---

### Architectures

<!-- "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." -->

The final blurry model contained two convolutional layers and two dense layers.

The final blinking model contained three convolutional layers, a dropout layer, and two dense layers.





---

### Results

<!-- "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." -->

At this time, the testing accuracy scores for the "blurry" models are 91.5% and 87.8% respectively.

I will be fine tuning these models in the upcoming weeks.





---

### Summary

<!-- "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." -->

At the beginning of this project I wanted to set ambitious goals to challenge myself. I ran put of time and I was not able to work out a model that identifies duplicate/similar photos. I will be working on this in the near future. Even though I didn't complete all my goals, I learned a great deal from this project.

I was able to build a basic application which sorts a folder of blurry and not blurry photographs into two  newly created folders. I'm very confident with some more time I can build out a fully functional app.

-----

### Demo (beta)

Here is a demo of the beta version of the application:

<!-- https://youtu.be/WJAJePCEY4Q -->

gifs.com/gif/app-demo-ZY4wX5

<iframe src='//gifs.com/embed/app-demo-ZY4wX5' frameborder='0' scrolling='no' width='576px' height='360px' style='-webkit-backface-visibility: hidden;-webkit-transform: scale(1);' ></iframe>

---
### Next steps

* Identify duplicate/similar photos by using a pixel similarity comparison in OpenCV, a clustering algorithm, or a combination of the two.
* Further develop the application into standalone functional software.
